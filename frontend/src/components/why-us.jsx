import React from "react";
import {ReactComponent as HandAndPlant} from "../icons/hand-plant-on-top.svg";
import {ReactComponent as Professionalism} from '../icons/hand-professionalism.svg'
import {ReactComponent as ManExpert} from '../icons/man-expert.svg';

function WhyUs() {
    return (
        <section class="why-us">
        <div class="container why-us__container">

            <div class="why-us__intro">
                <p class="why-us__subtitle">Nima uchun</p>
                <h2 class="why-us__title">
                    Bizni tanlashingiz shart
                </h2>
                <p class="why-us__description">
                    Xizmatlarimizdan foydalanishda quyidagi qulayliklarga va imkoniyatlarga ega bo’lasiz
                </p>
            </div>

            <div class="why-us__reasons">

                <div class="reasons__block">
                    <HandAndPlant />
                    <h3 class="reasons__block__title">
                        Tozalikdan rohatlanish
                    </h3>
                    <p class="reasons__block__description">
                        Biz sizning uyingiz va ofisingiz tozaligi va farovonligi uchun
                        keng ko'lamli xizmatlarni taqdim etamiz.
                    </p>
                </div>
                <div class="reasons__block">
                    <Professionalism />
                    <h3 class="reasons__block__title">
                        Professionallik
                    </h3>
                    <p class="reasons__block__description">
                        Biz sizning uyingiz va ofisingiz tozaligi va farovonligi uchun
                        keng ko'lamli xizmatlarni taqdim etamiz.
                    </p>
                </div>
                <div class="reasons__block">
                    <ManExpert />
                    <h3 class="reasons__block__title">
                        Mutaxassislar xizmati
                    </h3>
                    <p class="reasons__block__description">
                        Biz sizning uyingiz va ofisingiz tozaligi va farovonligi uchun
                        keng ko'lamli xizmatlarni taqdim etamiz.
                    </p>
                </div>

            </div>

        </div>
    </section>
    )
}

export default WhyUs;