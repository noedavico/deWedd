import { BrowserRouter, Route, Routes } from 'react-router-dom';
import {routes} from './routes/layout'

function App() {
  return (
    <BrowserRouter basename='/'>
     

      <Routes>
        { routes.map(route=> <Route {...route} key={route.path} />) }
      </Routes>

    
    </BrowserRouter>
  );
}

export default App;