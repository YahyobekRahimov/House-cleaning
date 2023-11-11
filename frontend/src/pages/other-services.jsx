import React from "react";
import Header from '../components/header';
import Contact from '../components/contact';
import Footer from '../components/footer';
import OtherServicesHero from "../components/OtherServicesHero";
import WhyUs from "../components/why-us";
import OtherServicesOffers from "../components/OtherServicesOffers";
import LiveChat from "../components/live-chat";


function OtherServices() {
    return (
        <>
            <Contact />
            <Header />
        <main>
            <OtherServicesHero />
            <WhyUs />
            <OtherServicesOffers />
            <LiveChat />
        </main>
            <Footer />
            <Contact />
        </>
    )
}

export default OtherServices;