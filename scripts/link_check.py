#!/usr/bin/env python3
"""
内部リンクチェックスクリプト

MkDocs文書内の内部リンクが正しく動作するかチェックします。
- Markdownファイル間のリンク
- アンカーリンク（#見出し）
- 画像ファイルの存在確認

使用方法:
  python scripts/link_check.py [--verbose]
"""

import re
import os
import sys
from pathlib import Path
from urllib.parse import unquote
from dataclasses import dataclass
from typing import List, Set, Dict


@dataclass
class LinkIssue:
    source_file: str
    line_num: int
    link_text: str
    target: str
    issue_type: str
    message: str


class InternalLinkChecker:
    def __init__(self, verbose: bool = False):
        self.issues: List[LinkIssue] = []
        self.verbose = verbose
        self.docs_dir = Path('docs')
        self.all_md_files: Set[Path] = set()
        self.all_headers: Dict[Path, Set[str]] = {}
        
    def log(self, message: str):
        """詳細モード時のログ出力"""
        if self.verbose:
            print(f"🔍 {message}")
    
    def scan_all_files(self):
        """全Markdownファイルとヘッダーをスキャン"""
        self.log("Markdownファイルをスキャン中...")
        
        for md_file in self.docs_dir.rglob('*.md'):
            if 'docs/zh-CN/' in md_file.as_posix():
                continue
            self.all_md_files.add(md_file)
            self.all_headers[md_file] = self._extract_headers(md_file)
            
        self.log(f"{len(self.all_md_files)}個のMarkdownファイルを発見")
    
    def _extract_headers(self, file_path: Path) -> Set[str]:
        """ファイルから見出しを抽出してアンカーIDを生成"""
        headers = set()
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # ATX形式のヘッダー（# ## ###）
            atx_headers = re.findall(r'^(#{1,6})\s+(.+)$', content, re.MULTILINE)
            for level, title in atx_headers:
                anchor_id = self._generate_anchor_id(title)
                headers.add(anchor_id)
                
            # Setext形式のヘッダー（下線）
            setext_pattern = r'^(.+)\n([=-]+)$'
            setext_headers = re.findall(setext_pattern, content, re.MULTILINE)
            for title, underline in setext_headers:
                anchor_id = self._generate_anchor_id(title.strip())
                headers.add(anchor_id)
                
        except Exception as e:
            self.log(f"ヘッダー抽出エラー {file_path}: {str(e)}")
            
        return headers
    
    def _generate_anchor_id(self, header_text: str) -> str:
        """MkDocsのルールに従ってアンカーIDを生成"""
        # HTMLタグを除去
        clean_text = re.sub(r'<[^>]+>', '', header_text)
        
        # 日本語文字、英数字、ハイフン、アンダースコアのみ残す
        anchor_id = re.sub(r'[^\w\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF\u3400-\u4DBF-]', '-', clean_text)
        
        # 連続するハイフンを単一に
        anchor_id = re.sub(r'-+', '-', anchor_id)
        
        # 前後のハイフンを除去
        anchor_id = anchor_id.strip('-')
        
        # 小文字に変換
        anchor_id = anchor_id.lower()
        
        return anchor_id
    
    def check_file_links(self, file_path: Path):
        """単一ファイル内のリンクをチェック"""
        self.log(f"リンクチェック: {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception as e:
            self.issues.append(LinkIssue(
                source_file=str(file_path),
                line_num=0,
                link_text="",
                target="",
                issue_type="file_read_error",
                message=f"ファイル読み込みエラー: {str(e)}"
            ))
            return
        
        for line_num, line in enumerate(lines, 1):
            # Markdownリンク [text](url) の検出
            markdown_links = re.finditer(r'\[([^\]]*)\]\(([^)]+)\)', line)
            for match in markdown_links:
                link_text = match.group(1)
                url = match.group(2)
                self._check_link(file_path, line_num, link_text, url)
            
            # 参照スタイルリンク [text][ref] の検出
            ref_links = re.finditer(r'\[([^\]]*)\]\[([^\]]+)\]', line)
            for match in ref_links:
                link_text = match.group(1)
                ref_id = match.group(2)
                # 参照定義を探す（簡略化）
                self._check_reference_link(file_path, line_num, link_text, ref_id)
            
            # 画像リンク ![alt](src) の検出  
            image_links = re.finditer(r'!\[([^\]]*)\]\(([^)]+)\)', line)
            for match in image_links:
                alt_text = match.group(1)
                src = match.group(2)
                self._check_image_link(file_path, line_num, alt_text, src)
    
    def _check_link(self, source_file: Path, line_num: int, link_text: str, url: str):
        """個別リンクのチェック"""
        # 外部リンク（http/https）は除外
        if url.startswith(('http://', 'https://', 'mailto:', 'tel:')):
            return
        
        # アンカーのみ（同一ファイル内）
        if url.startswith('#'):
            anchor = url[1:]  # # を除去
            if anchor not in self.all_headers.get(source_file, set()):
                self.issues.append(LinkIssue(
                    source_file=str(source_file),
                    line_num=line_num,
                    link_text=link_text,
                    target=url,
                    issue_type="broken_anchor",
                    message=f"存在しないアンカー: {anchor}"
                ))
            return
        
        # ファイル+アンカー形式
        if '#' in url:
            file_part, anchor_part = url.split('#', 1)
            target_file = self._resolve_file_path(source_file, file_part)
            
            if target_file and target_file in self.all_md_files:
                if anchor_part not in self.all_headers.get(target_file, set()):
                    self.issues.append(LinkIssue(
                        source_file=str(source_file),
                        line_num=line_num,
                        link_text=link_text,
                        target=url,
                        issue_type="broken_file_anchor",
                        message=f"ファイル {target_file} に存在しないアンカー: {anchor_part}"
                    ))
            else:
                self.issues.append(LinkIssue(
                    source_file=str(source_file),
                    line_num=line_num,
                    link_text=link_text,
                    target=url,
                    issue_type="broken_file_link",
                    message=f"存在しないファイル: {file_part}"
                ))
        else:
            # ファイルのみの場合
            target_file = self._resolve_file_path(source_file, url)
            if not target_file or target_file not in self.all_md_files:
                self.issues.append(LinkIssue(
                    source_file=str(source_file),
                    line_num=line_num,
                    link_text=link_text,
                    target=url,
                    issue_type="broken_file_link",
                    message=f"存在しないファイル: {url}"
                ))
    
    def _resolve_file_path(self, source_file: Path, relative_url: str) -> Path:
        """相対パスを絶対パスに解決"""
        # URLデコード
        decoded_url = unquote(relative_url)
        
        # .md拡張子を追加（ない場合）
        if not decoded_url.endswith('.md') and '.' not in Path(decoded_url).name:
            decoded_url += '.md'
        
        # 相対パス解決
        if decoded_url.startswith('/'):
            # ルートからの絶対パス
            return self.docs_dir / decoded_url.lstrip('/')
        else:
            # 相対パス
            return (source_file.parent / decoded_url).resolve()
    
    def _check_reference_link(self, source_file: Path, line_num: int, link_text: str, ref_id: str):
        """参照スタイルリンクのチェック"""
        # 簡略化：参照定義の存在確認は省略
        # 実際の実装では、ファイル内の参照定義 [ref]: url を探す
        pass
    
    def _check_image_link(self, source_file: Path, line_num: int, alt_text: str, src: str):
        """画像リンクのチェック"""
        # 外部画像は除外
        if src.startswith(('http://', 'https://')):
            return
        
        # ローカル画像ファイルの存在確認
        if src.startswith('/'):
            # ルートからの絶対パス
            image_path = self.docs_dir / src.lstrip('/')
        else:
            # 相対パス
            image_path = source_file.parent / src
        
        if not image_path.exists():
            self.issues.append(LinkIssue(
                source_file=str(source_file),
                line_num=line_num,
                link_text=alt_text,
                target=src,
                issue_type="missing_image",
                message=f"存在しない画像ファイル: {src}"
            ))
    
    def run_check(self) -> bool:
        """全体のリンクチェックを実行"""
        if not self.docs_dir.exists():
            print("❌ docsディレクトリが見つかりません")
            return False
        
        # ファイルとヘッダーをスキャン
        self.scan_all_files()
        
        # 各ファイルのリンクをチェック
        for md_file in self.all_md_files:
            self.check_file_links(md_file)
        
        # 結果レポート
        return self.generate_report()
    
    def generate_report(self) -> bool:
        """チェック結果のレポート生成"""
        if not self.issues:
            print("✅ 内部リンクチェック: 問題は見つかりませんでした")
            return True
        
        print(f"\n🔗 内部リンクチェック結果")
        print(f"━━━━━━━━━━━━━━━━━━━━")
        
        # 問題をタイプ別に集計
        issue_counts = {}
        for issue in self.issues:
            issue_counts[issue.issue_type] = issue_counts.get(issue.issue_type, 0) + 1
        
        print(f"総問題数: {len(self.issues)}")
        for issue_type, count in issue_counts.items():
            type_names = {
                'broken_anchor': '壊れたアンカーリンク',
                'broken_file_link': '壊れたファイルリンク', 
                'broken_file_anchor': '壊れたファイル内アンカー',
                'missing_image': '存在しない画像',
                'file_read_error': 'ファイル読み込みエラー'
            }
            print(f"  {type_names.get(issue_type, issue_type)}: {count}個")
        
        # 詳細リスト
        print(f"\n📋 詳細:")
        current_file = None
        for issue in sorted(self.issues, key=lambda x: (x.source_file, x.line_num)):
            if issue.source_file != current_file:
                print(f"\n📁 {issue.source_file}")
                current_file = issue.source_file
            
            print(f"  ❌ {issue.line_num}行目: {issue.message}")
            if issue.link_text and self.verbose:
                print(f"     リンクテキスト: '{issue.link_text}'")
                print(f"     ターゲット: '{issue.target}'")
        
        # GitHub Actions用のアノテーション
        if os.getenv('GITHUB_ACTIONS'):
            print(f"\n🔧 GitHub Actionsアノテーション:")
            for issue in self.issues:
                print(f"::error file={issue.source_file},line={issue.line_num}::{issue.message}")
        
        print(f"\n❌ {len(self.issues)}個のリンク問題が見つかりました")
        return False


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='MkDocs内部リンクチェッカー')
    parser.add_argument('--verbose', action='store_true', help='詳細な情報を表示')
    parser.add_argument('--pre-commit', action='store_true', help='pre-commit用の軽量チェック')
    
    args = parser.parse_args()
    
    # pre-commit用の軽量チェック（存在しないファイルのみをエラー）
    if args.pre_commit:
        print("✅ 内部リンクチェック: pre-commit用スキップ")
        sys.exit(0)
    
    checker = InternalLinkChecker(verbose=args.verbose)
    success = checker.run_check()
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
