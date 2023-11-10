import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import Services from './pages/Services';
import Blog from './pages/Blog';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" index element={<Home />} />
        <Route path="/services" element={<Services />} />
        <Route path='/blog' element={<Blog />} />
      </Routes>
    </Router>
  )
}

export default App;
