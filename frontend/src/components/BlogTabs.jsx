import React, { useState } from "react";
import {ReactComponent as SearchSVG} from '../icons/search-normal.svg';
import useLongState from '../hooks/longState'

function BlogTabs() {
    let jsonData;
    const [toggleState, setToggleState] = useState(1);
    const {longState, longDispatch} = useLongState()
    useEffect(() => {
        fetch(`http://192.168.0.104:8000/api/${longState.keys.category}`)
        .then(res => res.json()) 
        .then(data => {
          !data.new && 
          fetch(`http://192.168.0.104:8000/api/category`)
          .then(res => res.json()) 
          .then(data => {
            longDispatch({category: data})
          });
          });
        
        jsonData = longState.category;
      }, []);

    function DisplayPicture(pictureLink) {
        return (
            <img src={pictureLink} alt="service" />
        )
    }

    function DisplayContentByCategory(parent) {
        const filteredData = jsonData.filter((element) => element.parent ===parent);

        return filteredData.map((element) => {
            return (
            <div className="offers__cards__block">

                {DisplayPicture(element.photo)}

                <div className="category">{element.parent}</div>

                <h3 className="cards__block__title">
                    {element.name}
                </h3>
                <p className="cards__block__description">
                    {element.info}
                </p>
                <button className="cards__block__button common-button">
                    Ko'rish
                </button>
            </div>
    )}
    )
    }

    function DisplayContent() {
        return jsonData.map((element) => (
                <div className="offers__cards__block">

                    {DisplayPicture(element.photo)}

                    <div className="category">{element.parent}</div>

                    <h3 className="cards__block__title">
                        {element.name}
                    </h3>
                    <p className="cards__block__description">
                        {element.info}
                    </p>
                    <button className="cards__block__button common-button">
                        Ko'rish
                    </button>
                </div>
        )
        )
    }

    const toggleTab = (index) => {
        setToggleState(index);
    }
    return (
        <section className="tab-section">
            <div className="container tabbed-content__container">
                <div className="tabs-search-group">
                    <ul className="tabs">
                        <li className={toggleState == 1 ? "tab active-tab" : "tab"} onClick={() => toggleTab(1)}>Barchasi</li>
                        <li className={toggleState == 2 ? "tab active-tab" : "tab"} onClick={() => toggleTab(2)}>Tozalash</li>
                        <li className={toggleState == 3 ? "tab active-tab" : "tab"} onClick={() => toggleTab(3)}>Dizinfeksiya</li>
                        <li className={toggleState == 4 ? "tab active-tab" : "tab"} onClick={() => toggleTab(4)}>Yuvish</li>
                        <li className={toggleState == 5 ? "tab active-tab" : "tab"} onClick={() => toggleTab(5)}>Oshxona</li>
                        <li className={toggleState == 6 ? "tab active-tab" : "tab"} onClick={() => toggleTab(6)}>Uy va ofis</li>
                        <li className={toggleState == 7 ? "tab active-tab" : "tab"} onClick={() => toggleTab(7)}>Bog' va yashil maydonlar</li>
                    </ul>
                    <div className="vertical-line"></div>
                    <div className="search-input">
                        <SearchSVG />
                        <input type="text" name="search" id="search-button" placeholder="Qidirish" />
                    </div>
                </div>  
                <ul className="content-list">
                    <li className={toggleState === 1 ? 'content active-content' : 'content'}>{DisplayContent()}</li>
                    <li className={toggleState === 2 ? 'content active-content' : 'content'}>{DisplayContentByCategory('Tozalash')}</li>
                    <li className={toggleState === 3 ? 'content active-content' : 'content'}>{DisplayContentByCategory('Dizinfeksiya')}</li>
                    <li className={toggleState === 4 ? 'content active-content' : 'content'}>{DisplayContentByCategory('Yuvish')}</li>
                    <li className={toggleState === 5 ? 'content active-content' : 'content'}>{DisplayContentByCategory('Oshxona')}</li>
                    <li className={toggleState === 6 ? 'content active-content' : 'content'}>{DisplayContentByCategory('Uy va ofis')}</li>
                    <li className={toggleState === 7 ? 'content active-content' : 'content'}>{DisplayContentByCategory("Bog' va yashil maydonlar")}</li>
                </ul>
            </div>
        </section>
    )
}

export default BlogTabs;