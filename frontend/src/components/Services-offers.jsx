import React, { useState } from "react";

import jsonData from "../sources-from-backend/services-sources.json";

function DisplayPicture(pictureLink) {
  return <img src={pictureLink} alt="service" />;
}

let data = {
  services: [
    {
      id: 1,
      title: "Uylarni tozalash",
      description:
        "Biz sizning uyingiz va ofisingiz tozaligi va farovonligi uchun keng ko'lamli xizmatlarni taqdim etamiz.",
      picture: "https://picsum.photos/200",
    },
    {
      id: 2,
      title: "Ofislarni tozalash",
      description:
        "Biz sizning uyingiz va ofisingiz tozaligi va farovonligi uchun keng ko'lamli xizmatlarni taqdim etamiz.",
      picture: "https://picsum.photos/200",
    },
    {
      id: 3,
      title: "Bog’larni tozalash",
      description:
        "Biz sizning uyingiz va ofisingiz tozaligi va farovonligi uchun keng ko'lamli xizmatlarni taqdim etamiz.",
      picture: "https://picsum.photos/200",
    },
    {
      id: 4,
      title: "Yashil maydonlarni tozalash",
      description:
        "Biz sizning uyingiz va ofisingiz tozaligi va farovonligi uchun keng ko'lamli xizmatlarni taqdim etamiz.",
      picture: "https://picsum.photos/200",
    },
    {
      id: 5,
      title: "Qurilish joylarini tozalash",
      description:
        "Biz sizning uyingiz va ofisingiz tozaligi va farovonligi uchun keng ko'lamli xizmatlarni taqdim etamiz.",
      picture: "https://picsum.photos/200",
    },
    {
      id: 6,
      title: "Umumiy tozalash",
      description:
        "Biz sizning uyingiz va ofisingiz tozaligi va farovonligi uchun keng ko'lamli xizmatlarni taqdim etamiz.",
      picture: "https://picsum.photos/200",
    },
    {
      id: 7,
      title: "Mebellarni tozalash",
      description:
        "Biz sizning uyingiz va ofisingiz tozaligi va farovonligi uchun keng ko'lamli xizmatlarni taqdim etamiz.",
      picture: "https://picsum.photos/200",
    },
    {
      id: 8,
      title: "Mebellarni tozalash",
      description:
        "Biz sizning uyingiz va ofisingiz tozaligi va farovonligi uchun keng ko'lamli xizmatlarni taqdim etamiz.",
      picture: "https://picsum.photos/200",
    },
  ],
};

function ServicesOffers() {
  const [contentData, setData] = useState(data.services);
  return (
    <section className="offers">
      <div className="container offers__container">
        <div className="offers__intro">
          <div className="offers__intro__subtitle">Biz siz uchun</div>
          <h2 className="offers__intro__title">
            Qanday tozalash xizmatlar taklif qilamiz
          </h2>
          <p className="offers__intro__description">
            Biz sizning uyingiz, ofisingiz tozaligi va farovonligi uchun
            quyidagi xizmatlarni taklif qilamiz
          </p>
        </div>

        <div className="offers__cards">
          {contentData.map((item) => {
            return (
              <div className="offers__cards__block">
                {DisplayPicture(item.picture)}
                <h3 className="cards__block__title">{item.title}</h3>
                <p className="cards__block__description">{item.description}</p>
                <button className="cards__block__button common-button">
                  Batafsil
                </button>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}

export default ServicesOffers;
