import './SelectCurrencyWindow.css'
import fetchCurrencyTypes from "../../../api/FetchCurrencyTypes";
import currenciesRow from "../CurrenciesRow";
import {useEffect, useState} from "react";
import CurrenciesRow from "../CurrenciesRow";

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
          {currencies.map((currencyPair, index) => (
            <div key={index} className='currency-item'>
              <CurrenciesRow currencyPair={currencyPair}/>
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