import React from "react";
import Contact from "../components/contact";
import Header from "../components/header";
import Footer from "../components/footer";
import WhyUs from "../components/why-us";
import MobileApp from "../components/mobile-app";
import Feedbacks from "../components/feedbacks";
import Partners from "../components/partners";
import AboutHero from "../components/AboutHero";
import LiveChat from "../components/live-chat";

function About() {
    return (
        <>
            <Contact />
            <Header />
            <main>
                <AboutHero />
                <WhyUs />
                <MobileApp />
                <Feedbacks />
                <Partners />
                <LiveChat />
            </main>
            <Footer />
            <Contact />
        </>
    )
}

export default About;