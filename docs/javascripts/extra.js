// VRChat衣装制作ガイド - 追加JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // 進捗チェックリストの機能
    initProgressCheckboxes();
    
    // ページ内検索の改善
    improveSearch();
    
    // 外部リンクに新しいタブで開く属性を追加
    addTargetBlankToExternalLinks();

    // ヘッダーに言語切り替えボタンを追加
    initLanguageSwitch();
});

// 進捗チェックボックスの状態をローカルストレージに保存
function initProgressCheckboxes() {
    const checkboxes = document.querySelectorAll('.progress-checklist input[type="checkbox"]');
    
    checkboxes.forEach(function(checkbox, index) {
        const pageUrl = window.location.pathname;
        const checkboxId = `${pageUrl}_checkbox_${index}`;
        
        // 保存された状態を読み込み
        const savedState = localStorage.getItem(checkboxId);
        if (savedState === 'true') {
            checkbox.checked = true;
        }
        
        // チェック状態の変更を保存
        checkbox.addEventListener('change', function() {
            localStorage.setItem(checkboxId, checkbox.checked);
        });
    });
}

// 検索機能の改善（日本語検索対応）
function improveSearch() {
    const searchInput = document.querySelector('[data-md-component="search-query"]');
    if (searchInput) {
        searchInput.setAttribute('placeholder', 'ガイドを検索...');
    }
}

// 外部リンクを新しいタブで開く
function addTargetBlankToExternalLinks() {
    const links = document.querySelectorAll('a[href^="http"]:not([href*="' + window.location.hostname + '"])');
    links.forEach(function(link) {
        link.setAttribute('target', '_blank');
        link.setAttribute('rel', 'noopener noreferrer');
    });
}

// ソフトウェアバージョン情報の更新日時を表示
function updateVersionInfo() {
    const versionElements = document.querySelectorAll('.software-version');
    const lastUpdated = new Date().toLocaleDateString('ja-JP');
    
    versionElements.forEach(function(element) {
        element.setAttribute('title', `最終更新: ${lastUpdated}`);
    });
}

// ステップガイドのナビゲーション改善
function enhanceStepNavigation() {
    const steps = document.querySelectorAll('.step-container');
    steps.forEach(function(step, index) {
        step.setAttribute('id', `step-${index + 1}`);
    });
}

function initLanguageSwitch() {
    const headerInner = document.querySelector('.md-header__inner');
    if (!headerInner || headerInner.querySelector('.md-language-switch')) {
        return;
    }

    const switchConfig = getLanguageSwitchConfig();
    const wrapper = document.createElement('div');
    wrapper.className = 'md-header__option md-language-switch';

    const button = document.createElement('button');
    button.className = 'md-header__button md-icon md-language-switch__toggle';
    button.type = 'button';
    button.setAttribute('aria-label', switchConfig.title);
    button.setAttribute('title', switchConfig.title);
    button.setAttribute('aria-expanded', 'false');
    button.innerHTML = `${getGlobeIcon()}${getChevronIcon()}`;

    const menu = document.createElement('div');
    menu.className = 'md-language-switch__menu';
    menu.setAttribute('hidden', '');
    menu.appendChild(createLanguageOption('日本語', switchConfig.currentLanguage === 'ja' ? null : switchConfig.jaHref, switchConfig.currentLanguage === 'ja'));
    menu.appendChild(createLanguageOption('简体中文', switchConfig.currentLanguage === 'zh-CN' ? null : switchConfig.zhHref, switchConfig.currentLanguage === 'zh-CN'));

    wrapper.appendChild(button);
    wrapper.appendChild(menu);

    const paletteOption = headerInner.querySelector('[data-md-component="palette"]');
    const searchButton = headerInner.querySelector('label[for="__search"]');

    if (paletteOption) {
        paletteOption.insertAdjacentElement('afterend', wrapper);
    } else if (searchButton) {
        headerInner.insertBefore(wrapper, searchButton);
    } else {
        headerInner.appendChild(wrapper);
    }

    button.addEventListener('click', function(event) {
        event.stopPropagation();
        const isOpen = wrapper.classList.toggle('is-open');
        button.setAttribute('aria-expanded', String(isOpen));
        menu.hidden = !isOpen;
    });

    document.addEventListener('click', function(event) {
        if (!wrapper.contains(event.target)) {
            closeLanguageMenu(wrapper, button, menu);
        }
    });

    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape') {
            closeLanguageMenu(wrapper, button, menu);
        }
    });
}

function getLanguageSwitchConfig() {
    const pathname = window.location.pathname;
    const isChinesePage = /\/zh-CN(\/|$)/.test(pathname);
    const jaPath = isChinesePage
        ? pathname.replace(/\/zh-CN(\/|$)/, '/')
        : pathname;
    const zhPath = isChinesePage
        ? pathname
        : insertLanguageSegment(pathname, 'zh-CN');

    return {
        currentLanguage: isChinesePage ? 'zh-CN' : 'ja',
        jaHref: buildLanguageHref(jaPath),
        zhHref: buildLanguageHref(zhPath),
        title: isChinesePage ? '切换语言' : '言語を切り替え'
    };
}

function buildLanguageHref(pathname) {
    return `${window.location.origin}${pathname}${window.location.search}${window.location.hash}`;
}

function createLanguageOption(label, href, isCurrent) {
    const element = document.createElement(isCurrent ? 'span' : 'a');
    element.className = 'md-language-switch__option';
    if (isCurrent) {
        element.classList.add('is-current');
        element.setAttribute('aria-current', 'page');
    } else {
        element.href = href;
    }
    element.textContent = label;
    return element;
}

function closeLanguageMenu(wrapper, button, menu) {
    wrapper.classList.remove('is-open');
    button.setAttribute('aria-expanded', 'false');
    menu.hidden = true;
}

function getGlobeIcon() {
    return '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2m6.93 9h-3.09a15.7 15.7 0 0 0-1.38-5A8.03 8.03 0 0 1 18.93 11M12 4c.83 0 2.43 2.05 2.93 7H9.07C9.57 6.05 11.17 4 12 4M9.54 6a15.7 15.7 0 0 0-1.38 5H5.07A8.03 8.03 0 0 1 9.54 6M4.26 13h3.9a15.7 15.7 0 0 0 1.38 5 8.03 8.03 0 0 1-5.28-5M12 20c-.83 0-2.43-2.05-2.93-7h5.86c-.5 4.95-2.1 7-2.93 7m2.46-2a15.7 15.7 0 0 0 1.38-5h3.9a8.03 8.03 0 0 1-5.28 5Z"/></svg>';
}

function getChevronIcon() {
    return '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m7 10 5 5 5-5z"/></svg>';
}

function insertLanguageSegment(pathname, languageSegment) {
    const hasTrailingSlash = pathname.endsWith('/');
    const trimmedPath = pathname.replace(/\/+$/, '');
    const segments = trimmedPath.split('/').filter(Boolean);

    if (segments.length === 0) {
        return `/${languageSegment}/`;
    }

    const targetSegments = [segments[0], languageSegment].concat(segments.slice(1));
    const targetPath = `/${targetSegments.join('/')}`;
    return hasTrailingSlash ? `${targetPath}/` : targetPath;
}

// ページ読み込み完了時の追加処理
window.addEventListener('load', function() {
    updateVersionInfo();
    enhanceStepNavigation();
});
