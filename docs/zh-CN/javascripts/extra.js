// VRChat 服装制作指南 - 附加 JavaScript

document.addEventListener('DOMContentLoaded', function() {
    initProgressCheckboxes();
    improveSearch();
    addTargetBlankToExternalLinks();
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

window.addEventListener('load', function() {
    updateVersionInfo();
    enhanceStepNavigation();
});
