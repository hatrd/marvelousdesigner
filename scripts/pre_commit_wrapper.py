#!/usr/bin/env python3
"""
Pre-commit用ラッパースクリプト
引数処理の問題を解決し、docs/配下のファイルのみをチェック
"""

import sys
import os
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Usage: pre_commit_wrapper.py <script_name> <files...>")
        sys.exit(1)
    
    script_name = sys.argv[1]
    files = sys.argv[2:]
    
    # docs/ 配下のファイルのみにフィルタ
    docs_files = [
        f for f in files
        if f.startswith('docs/')
        and not f.startswith('docs/zh-CN/')
        and f.endswith('.md')
    ]
    
    if not docs_files:
        print(f"✅ {script_name}: 対象ファイルなし（docs/配下の.mdファイルのみ処理）")
        sys.exit(0)
    
    # スクリプト実行
    import subprocess
    
    for file_path in docs_files:
        cmd = ['/usr/bin/python3', f'scripts/{script_name}.py', '--file', file_path]
        
        # quality_check.pyの場合は--fixオプションを追加
        if script_name == 'quality_check':
            cmd.insert(-2, '--fix')
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"❌ {script_name}: {file_path}")
                if result.stderr:
                    print(result.stderr)
                if result.stdout:
                    print(result.stdout)
                sys.exit(1)
        except Exception as e:
            print(f"❌ {script_name} 実行エラー: {str(e)}")
            sys.exit(1)
    
    print(f"✅ {script_name}: {len(docs_files)}個のファイルをチェック完了")
    sys.exit(0)

if __name__ == '__main__':
    main()
