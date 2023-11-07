function giveButtonId() {
    const button = document.querySelector('.change-lang-button-wrapper > button');
    button.setAttribute('id', "change-lang-button");
}

function removeButtonId() {
    const button = document.querySelector('.change-lang-button-wrapper > button');
    button.removeAttribute('id');
}

function getPageLanguage() {
    const html = document.querySelector('html');
    return html.lang;
}

function getButtonsLanguage(button) {
    return button.getAttribute('class');    
}

function removeLangList() {
    const button = document.querySelector('.lang-list');
    button.classList.remove('display-block');
}

function placeSelectedLanguageButton(button) {
    removeButtonId();
    const referenceElement = document.querySelector('.lang-list')
    const parent = document.querySelector('.change-lang-button-wrapper');
    parent.insertBefore(button, referenceElement);
}
listeners();
function listeners() {
    const CHANGE_LANG_BUTTON = document.getElementById('change-lang-button');
    const LANG_LIST = document.querySelector('.lang-list');
    CHANGE_LANG_BUTTON.addEventListener('click', function() {
        LANG_LIST.classList.toggle('display-block');
    })
    
    const FIRST_LIST_BUTTON = document.querySelector('.first-list-item > button');
    console.log(FIRST_LIST_BUTTON);
    const SECOND_LIST_BUTTON = document.querySelector('.second-list-item > button');
    console.log(SECOND_LIST_BUTTON);
    FIRST_LIST_BUTTON.addEventListener('click', function() {
        let selectedLanguage = getButtonsLanguage(FIRST_LIST_BUTTON);
        const selectedLanguageButton = document.querySelector(`.${selectedLanguage}`);
        removeLangList();
        placeSelectedLanguageButton(selectedLanguageButton);
        const pageLanguageButton = document.querySelector(`.${getPageLanguage()}`);
        const FIRST_LIST_ITEM = document.querySelector('.first-list-item');
        FIRST_LIST_ITEM.appendChild(pageLanguageButton);
        giveButtonId();
        listeners()
    })
    SECOND_LIST_BUTTON.addEventListener('click', function() {
        let selectedLanguage = getButtonsLanguage(SECOND_LIST_BUTTON);
        const selectedLanguageButton = document.querySelector(`.${selectedLanguage}`);
        removeLangList();
        placeSelectedLanguageButton(selectedLanguageButton);
        const pageLanguageButton = document.querySelector(`.${getPageLanguage()}`)
        const SECOND_LIST_ITEM = document.querySelector('.second-list-item');
        SECOND_LIST_ITEM.appendChild(pageLanguageButton);
        giveButtonId();
        listeners();
    })
}

