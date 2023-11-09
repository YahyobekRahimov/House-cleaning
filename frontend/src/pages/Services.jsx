import Contact from "../components/contact";
import Header from "../components/header";
import BarMenu from "../components/bar-menu";
import ServicesHero from "../components/services-hero";
import '../styles/services.css';
import ServicesOffers from "../components/Services-offers";

function Services() {
  return (
    <>
      <Contact />
      <Header />
      <BarMenu />
      <main>
        <ServicesHero />
        <ServicesOffers /> 
      </main>
    </>
  );
}

export default Services;