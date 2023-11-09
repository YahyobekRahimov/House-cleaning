import React from "react";
import {ReactComponent as PhoneIcon} from '../icons/call.svg';
import {ReactComponent as Line} from '../icons/line.svg';
import {ReactComponent as YoutubeIcon} from '../icons/icon_youTube.svg';
import {ReactComponent as TelegramIcon} from '../icons/icon_telegram.svg';
import {ReactComponent as InstagramIcon} from '../icons/icon_instagram.svg';
const callNumber = 7757;

const workingTimeStart = `09:00`;
const workingTimeEnd = `18:00`;

const socialLinks = {
    "youtube": `https://youtube.com/house-cleaning`,
    "telegram": `https://t.me/house-cleaning`,
    "instagram": `https://instagram.com/house-cleaning`
}

function Contact() {
  return (
    <section className="contact">
      <div className="container contact__container">
        <div className="contact__information">
          <a href={`tel:${callNumber}`}>
            <PhoneIcon />
            <span className="phone-number">{callNumber}</span>
          </a>
          <Line/>
          <span className="information__action">
            Xizmatlarimiz haqida bepul ma’lumot olish uchun qo'ng'iroq qiling!
          </span>
          <Line/>
          <span className="work-time">Ish vaqti: {workingTimeStart} - {workingTimeEnd}</span>
        </div>
        <div className="contact__social-links">
          <a href={socialLinks["youtube"]} target="_blank">
            <YoutubeIcon />
          </a>
          <a href={socialLinks["telegram"]} target="_blank">
            <TelegramIcon />
          </a>
          <a href={socialLinks["instagram"]} target="_blank">
            <InstagramIcon />
          </a>
        </div>
      </div>
    </section>
  );
}

export default Contact;