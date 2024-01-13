import "./App.css";
import MainPageView from "./views/MainPageView";

import { ToastContainer } from "react-toastify";
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
