import React from 'react';
import './App.css';
import MainPageView from './views/MainPageView';
import { ToastContainer } from 'react-toastify'

function App() {
  return (
    <div className="App">
      <MainPageView />
      <ToastContainer />
    </div>
  );
}

export default App;
