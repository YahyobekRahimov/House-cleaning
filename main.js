
const body = document.querySelector('body');
const ul = document.querySelector('.header__nav');
const BAR_MENU = document.querySelector('.bar-menu__list');
const BARS = document.getElementById('bars');
const LIST_ITEMS = Array.from(ul.children);
const BAR_SECTION = document.querySelector('.bar-menu');
const hr = document.createElement('div');
const BAR_MENU_CONTAINER = document.querySelector('bar-menu__container');
hr.classList.add('bar-list__hr')
const hrCount = LIST_ITEMS.length - 1; 
const hrArray = [];

addNavLinksToBarMenu();

function addNavLinksToBarMenu() {
    if (determineSize() > 800) {
        return;
    }
    for (let i = 0; i < LIST_ITEMS.length; i++) {
        const element = LIST_ITEMS[i];
        const horizontalLine = hr.cloneNode(true);
        BAR_MENU.appendChild(element);
        if (i == LIST_ITEMS.length - 1) {
            break;
        }
        BAR_MENU.appendChild(horizontalLine);
    }
}

function disableScrolling() {
    body.classList.toggle('disable-scroll');
}

BARS.addEventListener('click', function() {
    BARS.classList.toggle('hamburger-x');
    BAR_SECTION.classList.toggle('bar-appear');
    disableScrolling();
})

function determineSize() {
    return window.innerWidth;
}