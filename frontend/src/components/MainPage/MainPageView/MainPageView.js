import "./MainPageView.css";
import React, {useEffect, useState} from "react";
import SelectCurrencyWindow from "../SelectCurrencyWindow";
import SaveButton from "../SaveButton";
import DownloadButton from "../DownloadButton";

const MainPageView = () => {
  const [selectedCurrencies, setSelectedCurrencies] = useState([]);
  const [successMessage, setSuccessMessage] = useState("")
  const [onSuccessfulSave, setOnSuccessfulSave] = useState(false);
  const handleSelectionChange = (newCurrencies) => {
    setSelectedCurrencies(newCurrencies);
  };

  const handleSuccessfulSave = () => {
    setOnSuccessfulSave(true)
    setSuccessMessage(`Data for ${selectedCurrencies.join(', ')} successfully saved to the server! ✔️`)
    setTimeout(() => {
      setOnSuccessfulSave(false)
    }, 5000)
  }

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
            onSuccessfulSave={handleSuccessfulSave}
            disabled={disableButton}/>
        </div>
      </div>

      {onSuccessfulSave && (
       <div className="save-status">
         {successMessage}
      </div>
      )}
    </div>
  );
};

export default MainPageView;