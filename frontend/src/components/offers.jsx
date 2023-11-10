import React from "react"
import GirlWasher1x from '../images/girl-washer-1x.png';
import GirlWasher2x from '../images/girl-washer-2x.png';
import GirlWasher3x from '../images/girl-washer-3x.png';

import DisinfectionGirl1x from "../images/disinfection-girl-1x.png";
import DisinfectionGirl2x from "../images/disinfection-girl-2x.png";
import DisinfectionGirl3x from "../images/disinfection-girl-3x.png";

import GirlHoldingTools1x from '../images/girl-holding-tools-1x.png';
import GirlHoldingTools2x from '../images/girl-holding-tools-2x.png';
import GirlHoldingTools3x from '../images/girl-holding-tools-3x.png';
function GirlWasher() {
    return (
        <picture>
            <source media="(min-width: 1200px)" srcSet={GirlWasher3x} />

            <source media="(min-width: 800px)" srcSet={GirlWasher2x} />

            <img src={GirlWasher1x} alt="Image Description" />
        </picture>
    )
}

function DisinfectionGirl() {
    return (
        
    <picture>
        <source media="(min-width: 1200px)" srcSet={DisinfectionGirl3x} />

        <source media="(min-width: 800px)" srcSet={DisinfectionGirl2x} />

        <img src={DisinfectionGirl1x} alt="Image Description" />
    </picture>
    )
}

function GirlHoldingTools() {
    return (
        
    <picture>
        <source media="(min-width: 1200px)" srcSet={GirlHoldingTools3x} />

        <source media="(min-width: 800px)" srcSet={GirlHoldingTools2x} />

        <img src={GirlHoldingTools1x} alt="Image Description" />
    </picture>
    )
}

function offers() {
    return (
        <section className="offers">
            <div className="container offers__container">

                <div className="offers__intro">

                    <div className="offers__intro__subtitle">
                        Biz siz uchun
                    </div>
                    <h2 className="offers__intro__title">
                        Nimalarni taklif qilamiz
                    </h2>
                    <p className="offers__intro__description">
                        Biz sizning uyingiz, ofisingiz tozaligi va farovonligi uchun quyidagi xizmatlarni taklif qilamiz
                    </p>

                </div>

                <div className="offers__cards">

                    <div className="offers__cards__block">
                        <GirlHoldingTools />
                        <h3 className="cards__block__title">
                            Tozalash xizmatlari
                        </h3>
                        <p className="cards__block__description">
                            Biz sizning uyingiz va ofisingiz tozaligi va farovonligi uchun keng ko'lamli xizmatlarni
                            taqdim etamiz.
                        </p>
                        <button className="cards__block__button common-button">
                            Batafsil
                        </button>

                    </div>

                    <div className="offers__cards__block">
                        <DisinfectionGirl />    
                        <h3 className="cards__block__title">
                            Dizinfeksiya xizmatlari
                        </h3>
                        <p className="cards__block__description">
                            Biz sizning uyingiz va ofisingiz tozaligi va farovonligi uchun keng ko'lamli xizmatlarni
                            taqdim etamiz.
                        </p>
                        <button className="cards__block__button common-button">
                            Batafsil
                        </button>

                    </div>

                    <div className="offers__cards__block">

                        <GirlWasher />
                        <h3 className="cards__block__title">
                            Yuvish xizmatlari
                        </h3>
                        <p className="cards__block__description">
                            Biz sizning uyingiz va ofisingiz tozaligi va farovonligi uchun keng ko'lamli xizmatlarni
                            taqdim etamiz.
                        </p>
                        <button className="cards__block__button common-button">
                            Batafsil
                        </button>

                    </div>

                </div>

            </div>
        </section>
    )
}

export default offers;