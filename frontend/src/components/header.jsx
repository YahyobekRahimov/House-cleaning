import React, { useState, useEffect } from "react";
import { Link } from 'react-router-dom';
import { ReactComponent as Logo } from "../icons/logo.svg";
import { ReactComponent as Sun } from "../icons/sun.svg";
import { ReactComponent as UzbekistanFlag } from "../icons/Uzbekistan.svg";
import { ReactComponent as RussianFlag } from "../icons/Russian-Federation.svg";
import { ReactComponent as BritainFlag } from "../icons/Great-Britain.svg";
import { ReactComponent as ArrowDown } from '../icons/arrow-down.svg';
import { useLongState } from "../hooks/longState";

function Header() {
  const [dark, setDark] = useState(false);
  useEffect(() => {
    const body = document.querySelector('body');
    body.classList.toggle('dark-theme');
  }, [dark] )
  function handleDarkTheme() {
    setDark(!dark)
  } 
  const {longState, longDispatch} = useLongState();
  function handleNavItem(page)  {
    longDispatch({navActive: page})
  }
  return (
    <header className="header">
      <section>
        <div className="container header__container">
          <button id="bars">
            <span className="first-bar"></span>
            <span className="middle-bar"></span>
            <span className="last-bar"></span>
          </button>
          <span onClick={() => handleNavItem('home')}>
            <Logo />
          </span>
          <nav>
            <ul className="header__nav">
              <li>
                <span>Xizmatlar <ArrowDown /></span>
                <ul className="HeaderDropdown">
                  <li onClick={() => handleNavItem('services')}>Tozalash xizmatlari</li>
                  <li onClick={() => handleNavItem('other-services')}>Boshqa xizmatlar</li>
                </ul>
              </li>
              <li onClick={() => handleNavItem('blog')}>
                Blog
              </li>
              <li onClick={() => handleNavItem('about')}>
                Biz haqimizda
              </li>
            </ul>
          </nav>
          <div className="header__features">
            <button id="change-theme-button" onClick={handleDarkTheme}>
              <Sun />
            </button>
            <div className="change-lang-button-wrapper">
              <button id="change-lang-button" className="uz">
                <UzbekistanFlag />
              </button>
              <ul className="lang-list">
                <li className="first-list-item">
                  <button className="ru">
                    <RussianFlag />
                  </button>
                </li>
                <li className="second-list-item">
                  <button className="en">
                    <BritainFlag />
                  </button>
                </li>
              </ul>
            </div>
            <button className="try-our-app-button common-button">
              Ilovamizni sinab ko'ring
            </button>
          </div>
        </div>
      </section>
    </header>
  );
}

export default Header;
