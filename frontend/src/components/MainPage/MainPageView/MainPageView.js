import './MainPageView.css';
import React, { useState, useEffect } from 'react';
import fetchExchangeRates from "../../../api/FetchExchangeRates";
import postRatesToSave from "../../../api/PostRatesToSave";
import SelectCurrencyWindow from "../SelectCurrencyWindow";

const MainPageView = () => {
  // const [exchangeRates, setExchangeRates] = useState([]);
  // useEffect(() => {
  //   const fetchData = async () => {
  //     const data = await fetchExchangeRates();
  //     setExchangeRates(data)
  //     console.log(data)
  //   };
  //
  //   fetchData();
  // }, []);
  //
  // useEffect(() => {
  //   const fetchData = async () => {
  //     const data = await postRatesToSave();
  //     console.log(data)
  //   };
  //
  //   fetchData();
  // }, []);

  return (
    <div className="content-div">
      <h2>Available currencies:</h2>
      <SelectCurrencyWindow />
    </div>
  );
};

export default MainPageView;