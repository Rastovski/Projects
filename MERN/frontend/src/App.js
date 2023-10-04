import Header from "./Header";
import {BrowserRouter, Routes, Route} from "react-router-dom"
import Home from "./Home";
import AddWorkout from "./AddWorkout"
const App = ()=>{
  return (
   <BrowserRouter>
    <Header />
    <Routes>
      <Route path="/" element={<Home />}></Route>
      <Route path="/addworkout" element={<AddWorkout />}></Route>

    </Routes>
   </BrowserRouter> 
  );
}

export default App;

