import jsonData from '../sources-from-backend/services-sources.json';

function DisplayPicture(pictureLink) {
    return (
        <img src={pictureLink} alt="service" />
    )
}


function ServicesOffers() {
    return (
        <section className="offers">
            <div className="container offers__container">

                <div className="offers__intro">

                    <div className="offers__intro__subtitle">
                        Biz siz uchun
                    </div>
                    <h2 className="offers__intro__title">
                        Qanday tozalash xizmatlar taklif qilamiz
                    </h2>
                    <p className="offers__intro__description">
                        Biz sizning uyingiz, ofisingiz tozaligi va farovonligi uchun quyidagi xizmatlarni taklif qilamiz    
                    </p>

                </div>

                <div className="offers__cards">

                    <div className="offers__cards__block">

                        {DisplayPicture(jsonData.services[0].picture)}
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

                        {DisplayPicture(jsonData.services[1].picture)}
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

                        {DisplayPicture(jsonData.services[2].picture)}
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

                        {DisplayPicture(jsonData.services[3].picture)}
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
                    <div className="offers__cards__block">

                        {DisplayPicture(jsonData.services[4].picture)}
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
                    <div className="offers__cards__block">

                        {DisplayPicture(jsonData.services[5].picture)}
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
                    <div className="offers__cards__block">

                        {DisplayPicture(jsonData.services[6].picture)}
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
                    <div className="offers__cards__block">

                        {DisplayPicture(jsonData.services[7].picture)}
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

export default ServicesOffers;