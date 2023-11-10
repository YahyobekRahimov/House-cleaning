import Contact from "../components/contact";
import Header from "../components/header";
import BarMenu from "../components/bar-menu";
import ServicesHero from "../components/services-hero";
import ServicesOffers from "../components/Services-offers";
import Footer from "../components/footer";
import LiveChat from "../components/live-chat";

function Services() {
  return (
    <>
      <Contact />
      <Header />
      <BarMenu />
      <main>
        <ServicesHero />
        <ServicesOffers /> 
        <LiveChat />
      </main>
      <Footer />
      <Contact />
    </>
  );
}

export default Services;