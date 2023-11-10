import React, { useState } from "react";
import {ReactComponent as SearchSVG} from '../icons/search-normal.svg';


function BlogTabs() {
    const [toggleState, setToggleState] = useState(1);
    const toggleTab = (index) => {
        console.log(index);
    }
    return (
        <section className="tab-section">
            <div className="container tabbed-content__container">
                <div className="tabs-search-group">
                    <ul className="tabs">
                        <li className={toggleState == 1 ? "tab active-tab" : "tabs"} onClick={() => toggleTab(1)}>Barchasi</li>
                        <li className={toggleState == 2 ? "tab active-tab" : "tabs"} onClick={() => toggleTab(2)}>Tozalash</li>
                        <li className={toggleState == 3 ? "tab active-tab" : "tabs"} onClick={() => toggleTab(3)}>Dizinfeksiya</li>
                        <li className={toggleState == 4 ? "tab active-tab" : "tabs"} onClick={() => toggleTab(4)}>Yuvish</li>
                        <li className={toggleState == 5 ? "tab active-tab" : "tabs"} onClick={() => toggleTab(5)}>Oshxona</li>
                        <li className={toggleState == 6 ? "tab active-tab" : "tabs"} onClick={() => toggleTab(6)}>Uy va ofis</li>
                        <li className={toggleState == 7 ? "tab active-tab" : "tabs"}onClick={() => toggleTab(7)}>Bog' va yashil maydonlar</li>
                    </ul>
                    <div className="vertical-line"></div>
                    <div className="search-input">
                        <SearchSVG />
                        <input type="text" name="search" id="search-button" placeholder="Qidirish" />
                    </div>
                </div>  
                <ul className="content">
                    <li className="content active-content"></li>
                </ul>
            </div>
        </section>
    )
}

export default BlogTabs;