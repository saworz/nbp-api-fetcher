import "./SelectCurrencyWindow.css";
import fetchCurrencyTypes from 'api/fetchCurrencyTypes';
import { useEffect, useState } from "react";
import CurrencyRow from "components/CurrencyRow";


interface ISelectCurrency {
  onCurrenciesChange: Function;
  selectedCurrencies: string[];
}

export const SelectCurrencyWindow: React.FC<ISelectCurrency> = ({ onCurrenciesChange, selectedCurrencies }) => {
  const [currencies, setCurrencies] = useState<string[]>();
  useEffect(() => {
    const fetchData = async () => {
      const data = await fetchCurrencyTypes();
      setCurrencies(data)
    };

    fetchData();
  }, []);

  const handleCheckboxChange = (currencyPair: string) => {
    const isSelected = selectedCurrencies.some(
      (selectedPair) => selectedPair === currencyPair
    );

    if (isSelected) {
      onCurrenciesChange((prevSelected: string[]) =>
        prevSelected.filter((selectedPair) => selectedPair !== currencyPair)
      );
    } else {
      onCurrenciesChange((prevSelected: string[]) => [...prevSelected, currencyPair]);
    }
  };

  return (
    <div className="window">
      {currencies !== undefined ? (
        <div className="currency-grid">
          {currencies.map((currencyPair, index) => (
            <div key={index} className="currency-row">
              <div className="exchange-type">
                <div>
                  <CurrencyRow currencyPair={currencyPair}/>
                </div>
                <div className="checkbox-container">
                  <input className="checkbox"
                         type="checkbox"
                         onChange={() => handleCheckboxChange(currencyPair)}
                  />
                </div>
              </div>
            </div>

          ))}
        </div>
      ) : (
        <div className='error-message'>
          Failed to load resources from the server 🥺
        </div>
      )}
    </div>
  );
};

export default SelectCurrencyWindow;

