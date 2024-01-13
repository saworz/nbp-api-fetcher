import "./MainPageView.css";
import React, { useState } from "react";
import SelectCurrencyWindow from "../../components/MainPage/SelectCurrencyWindow";
import SaveButton from "../../components/MainPage/SaveButton";
import DownloadButton from "../../components/MainPage/DownloadButton";

const MainPageView = () => {
  const [selectedCurrencies, setSelectedCurrencies] = useState([]);
  const handleSelectionChange = (newCurrencies) => {
    setSelectedCurrencies(newCurrencies);
  };

  const disableButton = selectedCurrencies.length === 0;

  return (
    <div className="content-div">
      <h2>Choose exchange rates to save:</h2>
      <SelectCurrencyWindow
        onCurrenciesChange={handleSelectionChange}
        selectedCurrencies={selectedCurrencies}/>

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