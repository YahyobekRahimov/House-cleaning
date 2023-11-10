import Home from './pages/Home';
import Services from './pages/Services';
import Blog from './pages/Blog';
import About from './pages/About';
import OtherServices from './pages/other-services';
import { useLongState } from './hooks/longState';



function App() {
  const {longState, longDispatch} = useLongState()
  return (
    <>
    {
      longState.navActive == "home" && <Home />  
    }
    {
      longState.navActive == "about" && <About />
    } 
    {
      longState.navActive == "services" && <Services />
    } 
    {
      longState.navActive == "blog" && <Blog />
    } 
    {
      longState.navActive == "other-services" && <OtherServices />
    } 
    </>
  )
}

export default App;
