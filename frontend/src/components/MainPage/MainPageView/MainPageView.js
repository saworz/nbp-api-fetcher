import "./MainPageView.css";
import React, { useState } from "react";
import SelectCurrencyWindow from "../SelectCurrencyWindow";
import SaveButton from "../SaveButton";
import DownloadButton from "../DownloadButton";

const MainPageView = () => {
  const [selectedCurrencies, setSelectedCurrencies] = useState([]);
  const handleSelectionChange = (newCurrencies) => {
    setSelectedCurrencies(newCurrencies);
  };

  const disableButton = selectedCurrencies.length === 0;

  return (
    <div className="content-div">
      <h2>Choose exchange rates to save:</h2>
      <SelectCurrencyWindow onCurrenciesChange={handleSelectionChange}/>

      <div className="buttons-field">
        <div className="single-button">
          <DownloadButton
            selectedCurrencies={selectedCurrencies}
            disabled={disableButton}/>
        </div>
        <div className="single-button">
          <SaveButton
            selectedCurrencies={selectedCurrencies}
            disabled={disableButton}/>
        </div>
      </div>
    </div>
  );
};

export default MainPageView;