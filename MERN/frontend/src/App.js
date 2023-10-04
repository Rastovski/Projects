import Header from "./components/Header";
import {BrowserRouter, Routes, Route} from "react-router-dom"
import Home from "./components/Home";
import AddWorkout from "./components/AddWorkout"
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

