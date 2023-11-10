import React from 'react';
import { ReactComponent as ArrowRight} from '../icons/arrow-right.svg';
import HeroGirl1x from '../images/hero-girl-1x.png';
import HeroGirl2x from '../images/hero-girl-2x.png';
import HeroGirl3x from '../images/hero-girl-3x.png';


function HeroImg() {
    return (
        <picture>

            <source media="(min-width: 1200px)" srcSet={HeroGirl3x} />

            <source media="(min-width: 800px)" srcSet={HeroGirl2x} />

            <img src="./images/hero-girl-1x.png" alt={HeroGirl1x} />
            
        </picture>
    )
}


function ServicesHero() {
    return (
        <section className="hero">

            <div className="container hero__site__map">
                <span>Bosh sahifa</span> 
                <ArrowRight />
                <span className="page-name">Xizmatlar</span>
            </div>
            <div className="container hero__container">
                <div className="hero__left-side">
                    <span className="hero__subheading">
                        Biz siz uchun
                    </span>
                    <h1 className="hero__title">
                        Toza va sog’lom muhit yaratamiz
                    </h1>
                    <p className="hero__description">
                        Biz sizning uyingiz va ofisingiz tozaligi va farovonligi uchun keng ko'lamli xizmatlarni taqdim
                        etamiz.
                    </p>
                    <div className="hero__button-group">
                        <button className="hero__contact-button common-button">
                            Bog'lanish
                        </button>
                        <button className="hero__services common-button">
                            Bizning xizmatlar
                        </button>
                    </div>
                </div>
                <HeroImg />
            </div>
        </section>
    )
}

export default ServicesHero;