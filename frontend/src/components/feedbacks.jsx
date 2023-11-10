import React, { useState } from "react";
import ClientImg from '../images/man-client.png'; // ! Here's client's image
import ClientImg2 from '../images/woman-client.png'; // ! Client's image

import YellowStar from '../icons/star.svg'; 
import GreyStar from '../icons/star-not-filled.svg';

import {ReactComponent as Quote} from '../icons/quote.svg';


function Client(imgSrc) {
    return <img className="client-img" src={imgSrc} alt="male client" />
}

let filledStarsClient1 = 4; // ! Number of yellow (filled) stars
let filledStarsClient2 = 2; // ! Number of yellow (filled) stars
let ClientFeedback1 = (`
Biz sizning uyingiz va ofisingiz tozaligi va farovonligi uchun keng ko'lamli xizmatlarni taqdim etamiz.`
) // ! Client's comment
let ClientFeedback2 = (
    `Biz sizning uyingiz va ofisingiz tozaligi va farovonligi uchun keng ko'lamli xizmatlarni taqdim etamiz.`
) // ! Client's comment 

let ClientName1 = `John Doe`;
let ClientName2 = `Sarah Miller`;

function Feedbacks() {
const [ratingForClient1, YellowStarsForClient1] = useState(filledStarsClient1);
const [ratingForClient2, YellowStarsForClient2] = useState(filledStarsClient2);

  function renderStars(rating) {
    const stars = [];
    for (let i = 0; i < 5; i++) {
      if (i < rating) {
        stars.push(<img key={i} src={YellowStar} alt="star" />);
      } else {
        stars.push(<img key={i} src={GreyStar} alt="star" />);
      }
    }
    return stars;
  }
    return (
        <section className="feedbacks">
            <div className="container feedbacks__container">

                <div className="feedbacks__intro">
                    <p className="feedbacks__subtitle">
                        Biz haqimizda
                    </p>
                    <h3 className="feedbacks__title">
                        Mijozlar nima deydi
                    </h3>
                </div>
                <div className="feedbacks-wrapper">
                    <div className="feedbacks__block">
                        <Quote />
                        <p className="feedbacks__text">
                           {ClientFeedback1}
                        </p>
                        {Client(ClientImg)}
                        <span className="client-name">
                            {ClientName1}
                        </span>
                        <div className="stars">
                            {renderStars(ratingForClient1)}
                        </div>
                    </div>

                    <div className="feedbacks__block">
                        <Quote />
                        <p className="feedbacks__text">
                            {ClientFeedback2}
                        </p>
                        {Client(ClientImg2)}
                        <span className="client-name">
                            {ClientName2}
                        </span>
                        <div className="stars">
                        {renderStars(ratingForClient2)}
                        </div>
                    </div>
                </div>

            </div>
        </section>
    )
}

export default Feedbacks;