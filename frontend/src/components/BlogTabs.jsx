import React, { useState } from "react";
import {ReactComponent as SearchSVG} from '../icons/search-normal.svg';

const jsonData = [
    {
        category: 'Tozalash',
        title: "Uylarni to'g'ri tozalash",
        description: "Biz sizning uyingiz va ofisingiz tozaligi va farovonligi uchun keng ko'lamli xizmatlarni taqdim etamiz.",
        image: "https://images.pexels.com/photos/48889/cleaning-washing-cleanup-the-ilo-48889.jpeg"
    },
    {
        category: 'Dizinfeksiya',
        title: "Uylarni to'g'ri tozalash",
        description: "Biz sizning uyingiz va ofisingiz tozaligi va farovonligi uchun keng ko'lamli xizmatlarni taqdim etamiz.",
        image: "https://images.pexels.com/photos/4239146/pexels-photo-4239146.jpeg",
    },
    {
        category: 'Yuvish',
        title: "Uylarni to'g'ri tozalash",
        description: "Biz sizning uyingiz va ofisingiz tozaligi va farovonligi uchun keng ko'lamli xizmatlarni taqdim etamiz.",
        image: "https://images.pexels.com/photos/48889/cleaning-washing-cleanup-the-ilo-48889.jpeg"
    },
    {
        category: 'Oshxona',
        title: "Uylarni to'g'ri tozalash",
        description: "Biz sizning uyingiz va ofisingiz tozaligi va farovonligi uchun keng ko'lamli xizmatlarni taqdim etamiz.",
        image: "https://images.pexels.com/photos/4239146/pexels-photo-4239146.jpeg",
    },
    {
        category: 'Uy va ofis',
        title: "Uylarni to'g'ri tozalash",
        description: "Biz sizning uyingiz va ofisingiz tozaligi va farovonligi uchun keng ko'lamli xizmatlarni taqdim etamiz.",
        image: "https://images.pexels.com/photos/48889/cleaning-washing-cleanup-the-ilo-48889.jpeg"
    },
    {
        category: "Bog' va yashil maydonlar",
        title: "Uylarni to'g'ri tozalash",
        description: "Biz sizning uyingiz va ofisingiz tozaligi va farovonligi uchun keng ko'lamli xizmatlarni taqdim etamiz.",
        image: "https://images.pexels.com/photos/4239146/pexels-photo-4239146.jpeg",
    },
    {
        category: 'Tozalash',
        title: "Uylarni to'g'ri tozalash",
        description: "Biz sizning uyingiz va ofisingiz tozaligi va farovonligi uchun keng ko'lamli xizmatlarni taqdim etamiz.",
        image: "https://images.pexels.com/photos/48889/cleaning-washing-cleanup-the-ilo-48889.jpeg"
    },
    {
        category: 'Tozalash',
        title: "Uylarni to'g'ri tozalash",
        description: "Biz sizning uyingiz va ofisingiz tozaligi va farovonligi uchun keng ko'lamli xizmatlarni taqdim etamiz.",
        image: "https://images.pexels.com/photos/4239146/pexels-photo-4239146.jpeg",
    },
]
function DisplayPicture(pictureLink) {
    return (
        <img src={pictureLink} alt="service" />
    )
}

function DisplayContentByCategory(category) {
    const filteredData = jsonData.filter((element) => element.category === category);

    return filteredData.map((element) => {
        return (
        <div className="offers__cards__block">

            {DisplayPicture(element.image)}

            <div className="category">{element.category}</div>

            <h3 className="cards__block__title">
                {element.title}
            </h3>
            <p className="cards__block__description">
                {element.description}
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

                {DisplayPicture(element.image)}

                <div className="category">{element.category}</div>

                <h3 className="cards__block__title">
                    {element.title}
                </h3>
                <p className="cards__block__description">
                    {element.description}
                </p>
                <button className="cards__block__button common-button">
                    Ko'rish
                </button>
            </div>
    )
    )
}

function BlogTabs() {
    const [toggleState, setToggleState] = useState(1);
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
                        <li className={toggleState == 7 ? "tab active-tab" : "tab"}onClick={() => toggleTab(7)}>Bog' va yashil maydonlar</li>
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