import './App.css';
import Contact from './components/contact';
import Header from './components/header';
import BarMenu from './components/bar-menu';
import LandingHero from './components/landing-hero';
import WhyUs from './components/why-us';
import Offers from './components/offers'; 
import MobileApp from './components/mobile-app';

function App() {
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
    </main>
    </>
  )
}

export default App;
