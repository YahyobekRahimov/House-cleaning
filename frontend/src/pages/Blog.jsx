import React from "react"
import Contact from "../components/contact"
import Header from "../components/header"
import BlogHero from "../components/BlogHero";
import BlogTabs from "../components/BlogTabs";
import Footer from '../components/footer';

function Blog() {
    return (
        <>
            <Contact />
            <Header />
        <main>
            <BlogHero />
            <BlogTabs /> 
        </main>
            <Footer />
            <Contact />
        </>
    )
}

export default Blog;