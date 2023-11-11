import React, {useEffect} from "react";
import { ReactComponent as ArrowRight } from "../icons/arrow-right.svg";
import useLongState from '../hooks/longState'

function AboutHero() {
  const {longState, longDispatch} = useLongState()
  let clients = 0
  let experience = 0
  useEffect(() => {
    fetch(`http://192.168.0.104:8000/api/${longState.keys.branch}`)
    .then(res => res.json()) 
    .then(data => {
      !data.new && 
      fetch(`http://192.168.0.104:8000/api/branch`)
      .then(res => res.json()) 
      .then(data => {
        longDispatch({branch: data})
      });
      });
    
    longState.branch.forEach(branch => {
    clients += parseInt(branch.clients);
    experience += parseInt(branch.experience);
  });
    clients = clients / clients.length
    experience = experience / experience.length
    
  }, []);

  return (
    <section className="About__hero">
      <div className="container About__Hero__site__map">
        <span>Bosh sahifa</span>
        <ArrowRight />
        <span className="page-name">Biz haqimizda</span>
      </div>
      <div className="container About__Hero__container">
        <div className="About__Hero__left-side">
          <span className="About__Hero__subheading">Toza makon</span>
          <h1 className="About__Hero__title">Biz haqimizda</h1>
          <p className="About__Hero__description">
            Biz sizning uyingiz va ofisingiz tozaligi va farovonligi uchun keng
            ko'lamli xizmatlarni taqdim etamiz.
          </p>
          <div className="stats-wrapper">
            <div className="stats">
              <span className="stats-description">Mijozlarimiz</span>
              <span className="stats-number">{clients}+</span>
            </div>
            <div className="stats">
              <span className="stats-description">Ish tajribamiz</span>
              <span className="stats-number">{experience} yil</span>
            </div>
          </div>
        </div>
        <div className="iframe-wrapper">
          <iframe
            allowFullScreen="allowFullScreen"
            src="https://www.youtube.com/embed/Ad7mZ16ACB0?ecver=1&amp;iv_load_policy=1&amp;yt:stretch=16:9&amp;autohide=1&amp;color=red&amp;width=560&amp;width=560"
            width="560"
            height="315"
            allowtransparency="true"
            frameborder="0"
          ></iframe>
        </div>
      </div>
    </section>
  );
}

export default AboutHero;
