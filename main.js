// ! Initial variables
const BAR_MENU = document.querySelector(".bar-menu__list");
const BAR_MENU_CONTAINER = document.querySelector("bar-menu__container");
const UL = document.querySelector(".header__nav");
const BODY = document.querySelector("body");
const BARS = document.getElementById("bars");
const BAR_SECTION = document.querySelector(".bar-menu");
const hr = document.createElement("div");
const LIST_ITEMS = Array.from(UL.children);

// language related images
hr.classList.add("bar-list__hr");
const hrCount = LIST_ITEMS.length - 1;
const hrArray = [];
addNavLinksToBarMenu();

function scrollToTop() {
  window.scrollTo({
    top: 0
  });
}

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
  BODY.classList.toggle("disable-scroll");
}

BARS.addEventListener("click", function () {
  BARS.classList.toggle("hamburger-x");
  BAR_SECTION.classList.toggle("bar-appear");
  scrollToTop();
  disableScrolling();
});

function determineSize() {
  return window.innerWidth;
}

const header = document.querySelector('header');
const headerOffset = header.offsetTop;
function handleScroll() {
  if (window.pageYOffset > headerOffset) {
    header.classList.add('fixed-header');
  } else {
    header.classList.remove('fixed-header');
  }
}

window.addEventListener('scroll', handleScroll);