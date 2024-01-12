import './MainPageView.css';
import React, { useState, useEffect } from 'react';
import SelectCurrencyWindow from "../SelectCurrencyWindow";
import SaveButton from "../SaveButton";
import PreviewButton from "../PreviewButton";

const MainPageView = () => {
  const [selectedCurrencies, setSelectedCurrencies] = useState([]);
  const handleSelectionChange = (newCurrencies) => {
    setSelectedCurrencies(newCurrencies);
  };

  useEffect(() => {
    console.log("In parent folder")
    console.log('Selected Currencies changed:', selectedCurrencies);
  }, [selectedCurrencies]);

  return (
    <div className="content-div">
      <h2>Choose exchange rates to save:</h2>
      <SelectCurrencyWindow onCurrenciesChange={handleSelectionChange}/>

      <div className="buttons-field">
        <div className="single-button">
          <PreviewButton selectedCurrencies={selectedCurrencies}/>
        </div>
        <div className="single-button">
          <SaveButton />
        </div>
      </div>
    </div>
  );
};

export default MainPageView;