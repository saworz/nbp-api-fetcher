import "./App.css";
import MainPageView from "./components/MainPage/MainPageView";

import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

function App() {
  return (
    <div className="app">
      <MainPageView />
      <ToastContainer />
    </div>
  );
}

export default App;
