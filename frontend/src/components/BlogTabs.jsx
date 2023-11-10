import React, { useState } from "react";


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
                        <li className="tab active-tab" onClick={() => toggleTab(1)}>Barchasi</li>
                        <li className='tab'>Tozalash</li>
                        <li className='tab'>Dizinfeksiya</li>
                        <li className='tab'>Yuvish</li>
                        <li className='tab'>Oshxona</li>
                        <li className='tab'>Uy va ofis</li>
                        <li className='tab'>Bog' va yashil maydonlar</li>
                    </ul>
                    <div className="vertical-line"></div>
                    <input type="text" name="search" id="search-button" placeholder="Qidirish" />
                </div>  
                <div className="content">
                    <div className="content1 active-content">

                    </div>
                    <div className="content2">

                    </div>
                </div>
            </div>
        </section>
    )
}

export default BlogTabs;