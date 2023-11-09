import LandingHero from '../components/landing-hero';
import WhyUs from '../components/why-us';
import Offers from '../components/offers'; 
import MobileApp from '../components/mobile-app';
import Feedbacks from '../components/feedbacks';
import Partners from '../components/partners';
import Footer from '../components/footer'; 
import Contact from '../components/contact';
import Header from '../components/header';
import BarMenu from '../components/bar-menu';
import '../styles/index.css';

function Home() {
    return (
    <>
        <Contact />
        <Header />
        <BarMenu />
      <main>
        <LandingHero />
        <WhyUs />
        <Offers />
        <MobileApp />
        <Feedbacks />
        <Partners />
      </main>
      <Footer />
      <Contact />
      </>
    )
  }
  
export default Home;