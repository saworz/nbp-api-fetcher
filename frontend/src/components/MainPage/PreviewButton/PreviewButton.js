import './PreviewButton.css'
import { useState, useEffect } from "react";
import fetchExchangeRates from "../../../api/FetchExchangeRates";

export const PreviewButton = ({ selectedCurrencies }) => {
  const [exchangeRates, setExchangeRates] = useState();

  useEffect(() => {
    if (exchangeRates) {
      console.log(exchangeRates)
    }

  }, [exchangeRates]);

  const fetchData = async () => {
    try {
      const data = await fetchExchangeRates(selectedCurrencies);
      setExchangeRates(data);
    } catch (error) {
      console.error('Error fetching exchange rates:', error)
    }
  };

  const handlePreviewClick = async () => {
    // await fetchData();
    console.log('click')
  };

  return (
    <div>
      <button onClick={handlePreviewClick}>Preview Exchange Rates</button>
    </div>
  );
};

export default PreviewButton;