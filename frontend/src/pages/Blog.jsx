import React from "react"
import Contact from "../components/contact"
import Header from "../components/header"
import BlogHero from "../components/BlogHero";
import BlogTabs from "../components/BlogTabs";

function Blog() {
    return (
        <>
            <Contact />
            <Header />
        <main>
            <BlogHero />
            <BlogTabs /> 
        </main>
        </>
    )
}

export default Blog;