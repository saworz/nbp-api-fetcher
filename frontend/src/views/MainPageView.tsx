import SelectCurrencyWindow from "components/SelectCurrencyWindow";
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
            Download button
        </div>
        <div className="single-button">
            Save button
        </div>
      </div>
    </div>
  );
};

export default MainPageView;