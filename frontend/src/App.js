import './App.css';
import Welcome from './Components/Welcome';
import Scarypage from './Components/Scarypage';
import Imagespage from './Components/Imagespage';
import { BrowserRouter, Routes, Route } from "react-router-dom";


function App() {
  return (
    <>
      <div>
        <BrowserRouter>
      <Routes>
        {/* <Route path="/" element={<Welcome />}> */}
          <Route path="/" element={<Welcome />} />
          <Route path="/scary" element={<Scarypage />} />
          <Route path="/image" element={<Imagespage />} />
          {/* <Route path="/funny" element={<Funnypage />} /> */}
          {/* <Route path="*" element={<NoPage />} /> */}
        {/* </Route> */}
      </Routes>
    </BrowserRouter>
          
          {/* <Welcome /> */}

          {/* <Scarypage /> */}
          {/* <Funnypage /> */}

      </div>
    </>
  );
}

export default App;
