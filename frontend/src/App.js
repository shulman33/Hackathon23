import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import WelcomePage from "./Pages/WelcomePage";
import SignIn from "./Pages/SignIn";
import SignUp from "./Pages/SignUp";
import './Pages/style.css';

function App() {
  return (
    <div>
      <Router>
        <Routes>
          <Route path="/" element={<WelcomePage />} />
          <Route path="/signin" element={<SignIn />} />
          <Route path="/signup" element={<SignUp />} />
        </Routes>
      </Router>
    </div>
  );
 }
 
export default App;
