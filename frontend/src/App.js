import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import Services from './pages/Services';
import Blog from './pages/Blog';
import About from './pages/About';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" index element={<Home />} />
        <Route path="/services" element={<Services />} />
        <Route path='/blog' element={<Blog />} />
        <Route path='/about' element={<About />} /> 
      </Routes>
    </Router>
  )
}

export default App;
