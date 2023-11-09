import React from "react";
import {ReactComponent as Logo} from '../icons/logo.svg';
import {ReactComponent as Sun} from '../icons/sun.svg';
import {ReactComponent as UzbekistanFlag} from '../icons/Uzbekistan.svg';
import {ReactComponent as RussianFlag} from '../icons/Russian-Federation.svg';
import {ReactComponent as BritainFlag} from '../icons/Great-Britain.svg';


const Header = () => (
    <header className="header">
    <section>
        <div className="container header__container">
            <button id="bars">
                <span className="first-bar"></span>
                <span className="middle-bar"></span>
                <span className="last-bar"></span>
            </button>
            <a href="#">
                <Logo />
            </a>
            <nav>
                <ul className="header__nav">
                    <li>
                        <a href="#">
                            Xizmatlar
                        </a>
                    </li>
                    <li>
                        <a href="#">Blog</a>
                    </li>
                    <li>
                        <a href="#">Biz haqimizda</a>
                    </li>
                </ul>
            </nav>
            <div className="header__features">
                <button id="change-theme-button">
                    <Sun />
                </button>
                <div className="change-lang-button-wrapper">
                    <button id="change-lang-button" className="uz">
                        <UzbekistanFlag />
                    </button>
                    <ul className="lang-list">
                        <li className="first-list-item">
                            <button className="ru"><RussianFlag /></button>
                        </li>
                        <li className="second-list-item">
                            <button className="en"><BritainFlag /></button>
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
)

export default Header;