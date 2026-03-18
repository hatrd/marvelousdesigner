// VRChat 服装制作指南 - 附加 JavaScript

document.addEventListener('DOMContentLoaded', function() {
    initProgressCheckboxes();
    improveSearch();
    addTargetBlankToExternalLinks();
    initLanguageSwitch();
});

function initProgressCheckboxes() {
    const checkboxes = document.querySelectorAll('.progress-checklist input[type="checkbox"]');

    checkboxes.forEach(function(checkbox, index) {
        const pageUrl = window.location.pathname;
        const checkboxId = `${pageUrl}_checkbox_${index}`;
        const savedState = localStorage.getItem(checkboxId);
        if (savedState === 'true') {
            checkbox.checked = true;
        }

        checkbox.addEventListener('change', function() {
            localStorage.setItem(checkboxId, checkbox.checked);
        });
    });
}

function improveSearch() {
    const searchInput = document.querySelector('[data-md-component="search-query"]');
    if (searchInput) {
        searchInput.setAttribute('placeholder', '搜索指南...');
    }
}

function addTargetBlankToExternalLinks() {
    const links = document.querySelectorAll('a[href^="http"]:not([href*="' + window.location.hostname + '"])');
    links.forEach(function(link) {
        link.setAttribute('target', '_blank');
        link.setAttribute('rel', 'noopener noreferrer');
    });
}

function updateVersionInfo() {
    const versionElements = document.querySelectorAll('.software-version');
    const lastUpdated = new Date().toLocaleDateString('zh-CN');

    versionElements.forEach(function(element) {
        element.setAttribute('title', `最后更新：${lastUpdated}`);
    });
}

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
    button.innerHTML = getGlobeIcon();

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
    return '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-10 10a10 10 0 0 0 10 10a10 10 0 0 0 10-10A10 10 0 0 0 12 2m6.92 6h-3.95a15.5 15.5 0 0 0-1.38-3.56A8.03 8.03 0 0 1 18.92 8M12 4.04c.83 1.2 1.51 2.51 2.02 3.96H9.98A15.6 15.6 0 0 1 12 4.04M4.26 14A8.07 8.07 0 0 1 4 12c0-.7.09-1.37.26-2h4.16c-.09.65-.14 1.31-.14 2s.05 1.35.14 2M5.08 16h3.95c.36 1.3.82 2.5 1.38 3.56A8.03 8.03 0 0 1 5.08 16M8.04 12c0-.68.06-1.35.16-2h7.6c.1.65.16 1.32.16 2s-.06 1.35-.16 2H8.2A13.8 13.8 0 0 1 8.04 12m3.96 7.96A15.6 15.6 0 0 1 9.98 16h4.04A15.6 15.6 0 0 1 12 19.96M13.59 19.56c.56-1.06 1.02-2.26 1.38-3.56h3.95a8.03 8.03 0 0 1-5.33 3.56M15.58 14c.09-.65.14-1.31.14-2s-.05-1.35-.14-2h4.16c.17.63.26 1.3.26 2s-.09 1.37-.26 2z"/></svg>';
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

window.addEventListener('load', function() {
    updateVersionInfo();
    enhanceStepNavigation();
});
