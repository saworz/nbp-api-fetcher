import './SelectCurrencyWindow.css'
import fetchCurrencyTypes from "../../../api/FetchCurrencyTypes";
import {useEffect, useState} from "react";
import CurrenciesRow from "../CurrenciesRow";

export const SelectCurrencyWindow = ({ onCurrenciesChange }) => {
  const [currencies, setCurrencies] = useState();
  useEffect(() => {
    const fetchData = async () => {
      const data = await fetchCurrencyTypes();
      setCurrencies(data)
    };

    fetchData();
  }, []);

  const [selectedCurrencies, setSelectedCurrencies] = useState([]);

  useEffect(() => {
    onCurrenciesChange(selectedCurrencies);
  }, [selectedCurrencies]);


  const handleCheckboxChange = (currencyPair) => {
    const isSelected = selectedCurrencies.some((selectedPair) => (
      selectedPair === currencyPair
    ));

    if (isSelected) {
      setSelectedCurrencies((prevSelected) => (
        prevSelected.filter((selectedPair) => selectedPair !== currencyPair)
      ));
    } else {
      setSelectedCurrencies((prevSelected) => [...prevSelected, currencyPair]);
    }
  };

  return (
    <div className='window'>
      {currencies !== undefined ? (
        <div className='currency-grid'>
          {currencies.map((currencyPair, index) => (
            <div key={index} className='currency-row'>
              <div className='exchange-type'>
                <CurrenciesRow currencyPair={currencyPair}/>
              </div>
              <input className="checkbox"
                type="checkbox"
                onChange={() => handleCheckboxChange(currencyPair)}
              />
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