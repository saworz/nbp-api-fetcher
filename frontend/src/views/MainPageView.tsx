import SelectCurrencyWindow from "components/SelectCurrencyWindow";
import SaveButton from "components/Buttons/SaveButton";
import DownloadButton from "components/Buttons/DownloadButton";
import { useState } from "react";
import "./MainPageView.css";

const MainPageView: React.FC = () => {
  
  const [selectedCurrencies, setSelectedCurrencies] = useState<string[]>([]);
  const handleSelectionChange = (newCurrencies: string[]) => {
    setSelectedCurrencies(newCurrencies);
  };

  const disableButton = selectedCurrencies.length === 0;

  return (
    <div className="content-div">
      <h2>Choose exchange rates to save:</h2>
      <SelectCurrencyWindow 
        onCurrenciesChange={handleSelectionChange}
        selectedCurrencies={selectedCurrencies}
      />

      <div className="buttons-field">
        <div className="single-button">
          <DownloadButton
            selectedCurrencies={selectedCurrencies}
            disabled={disableButton}
          />
        </div>
        <div className="single-button">
          <SaveButton
            selectedCurrencies={selectedCurrencies}
            disabled={disableButton}
          />
        </div>
      </div>
    </div>
  );
};

export default MainPageView;