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
    wrapper.className = 'md-header__option';

    const link = document.createElement('a');
    link.className = 'md-header__button md-icon md-language-switch';
    link.href = switchConfig.href;
    link.textContent = switchConfig.label;
    link.setAttribute('aria-label', switchConfig.title);
    link.setAttribute('title', switchConfig.title);

    wrapper.appendChild(link);

    const paletteOption = headerInner.querySelector('[data-md-component="palette"]');
    const searchButton = headerInner.querySelector('label[for="__search"]');

    if (paletteOption) {
        paletteOption.insertAdjacentElement('afterend', wrapper);
    } else if (searchButton) {
        headerInner.insertBefore(wrapper, searchButton);
    } else {
        headerInner.appendChild(wrapper);
    }
}

function getLanguageSwitchConfig() {
    const pathname = window.location.pathname;
    const isChinesePage = /\/zh-CN(\/|$)/.test(pathname);
    const targetPath = isChinesePage
        ? pathname.replace(/\/zh-CN(\/|$)/, '/')
        : insertLanguageSegment(pathname, 'zh-CN');

    return {
        href: `${window.location.origin}${targetPath}${window.location.search}${window.location.hash}`,
        label: isChinesePage ? '日' : '中',
        title: isChinesePage ? '切换到日文页面' : '日本語ページに切り替え'
    };
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
