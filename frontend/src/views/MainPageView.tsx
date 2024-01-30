import SelectCurrencyWindow from "components/SelectCurrencyWindow";
import "./MainPageView.css";

const MainPageView: React.FC = () => {

  return (
    <div className="content-div">
      <h2>Choose exchange rates to save:</h2>
      <SelectCurrencyWindow />

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