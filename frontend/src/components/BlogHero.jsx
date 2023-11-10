import React from "react"
import { ReactComponent as ArrowRight} from '../icons/arrow-right.svg';

function BlogHero() {
    return (
        <section className="blogHero">

            <div className="container blogHero__site__map">
                <span>Bosh sahifa</span> 
                <ArrowRight />
                <span className="page-name">Blog</span>
            </div>
            <div className="container blogHero__container">
                <div className="blogHero__left-side">
                    <span className="blogHero__subheading">
                        Biz siz uchun
                    </span>
                    <h1 className="blogHero__title">
                        Toza va sog’lom muhit yaratamiz
                    </h1>
                    <p className="blogHero__description">
                        Biz sizning uyingiz va ofisingiz tozaligi va farovonligi uchun keng ko'lamli xizmatlarni taqdim
                        etamiz.
                    </p>
                    <div className="blogHero__button-group">
                        <button className="blogHero__contact-button common-button">
                            Bog'lanish
                        </button>
                        <button className="blogHero__services common-button">
                            Bizning xizmatlar
                        </button>
                    </div>
                </div>
            </div>
        </section>
    )
}

export default BlogHero;