import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import Services from './pages/Services';
import Blog from './pages/Blog';
import About from './pages/About';
import OtherServices from './pages/other-services';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" index element={<Home />} />
        <Route path="/services" element={<Services />} />
        <Route path='/blog' element={<Blog />} />
        <Route path='/about' element={<About />} /> 
        <Route path='/other-services' element={<OtherServices />} /> 
      </Routes>
    </Router>
  )
}

export default App;
