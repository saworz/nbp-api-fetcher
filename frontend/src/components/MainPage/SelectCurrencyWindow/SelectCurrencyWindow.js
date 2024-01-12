import './SelectCurrencyWindow.css'
import fetchCurrencyTypes from "../../../api/FetchCurrencyTypes";
import {useEffect, useState} from "react";

export const SelectCurrencyWindow = () => {
  const [currencies, setCurrencies] = useState();
  useEffect(() => {
    const fetchData = async () => {
      const data = await fetchCurrencyTypes();
      setCurrencies(data)
      console.log(data)
    };

    fetchData();
  }, []);


  return (
    <div className='window'>
      {currencies !== undefined ? (
        <div className='currency-grid'>
          {currencies.map((currency, index) => (
            <div key={index} className='currency-item'>
              {currency}
            </div>
          ))}
        </div>
      ) : (
        <p>Loading currencies...</p>
      )}
    </div>
  );
};

export default SelectCurrencyWindow;