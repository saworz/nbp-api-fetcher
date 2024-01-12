import './MainPageView.css';
import React, { useState, useEffect } from 'react';
import fetchCurrencyTypes from "../../../api/FetchCurrencyTypes";
import fetchExchangeRates from "../../../api/FetchExchangeRates";

const MainPageView = () => {
  const [currencies, setCurrencies] = useState([]);
  useEffect(() => {
    const fetchData = async () => {
      const data = await fetchCurrencyTypes();
      setCurrencies(data)
      console.log(data)
    };

    fetchData();
  }, []);

  const [exchangeRates, setExchangeRates] = useState([]);
  useEffect(() => {
    const fetchData = async () => {
      const data = await fetchExchangeRates();
      setExchangeRates(data)
      console.log(data)
    };

    fetchData();
  }, []);

  return (
    <div className="content-div">
      <h2>Available currencies:</h2>
    </div>
  );
};

export default MainPageView;