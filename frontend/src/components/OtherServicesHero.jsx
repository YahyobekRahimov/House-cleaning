import React from "react";
import { ReactComponent as ArrowRight } from "../icons/arrow-right.svg";

function OtherServicesHero() {
    return (
              <section className="About__hero">
                <div className="container About__Hero__site__map">
                  <span>Bosh sahifa</span>
                  <ArrowRight />
                  <span className="page-name">Boshqa xizmatlar</span>
                </div>
                <div className="container About__Hero__container">
                  <div className="hero__left-side">
                    <span className="hero__subheading">Biz siz uchun</span>
                    <h1 className="hero__title">
                      Uylarni tozalash xizmatini 
                      taklif qilamiz  
                    </h1>
                    <p className="hero__description">
                       Biz sizning uyingiz va ofisingiz tozaligi va farovonligi uchun keng ko'lamli xizmatlarni taqdim etamiz.
                    </p>
                    <div className="hero__button-group">
                          <button className="hero__contact-button common-button">
                            Buyurtma qilish
                          </button>
                          <button className="hero__services common-button">
                            Konsultatsiya olish
                          </button>
                    </div>
                  </div>
                  <div className="iframe-wrapper">
                    <iframe
                      allowFullScreen="allowFullScreen"
                      src="https://www.youtube.com/embed/Ad7mZ16ACB0?ecver=1&amp;iv_load_policy=1&amp;yt:stretch=16:9&amp;autohide=1&amp;color=red&amp;width=560&amp;width=560"
                      width="560"
                      height="315"
                      frameborder="0"
                    ></iframe>
                  </div>
                </div>
              </section>
              )
}

export default OtherServicesHero;