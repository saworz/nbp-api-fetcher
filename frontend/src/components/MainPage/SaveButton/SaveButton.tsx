import "./SaveButton.css"
import { toast } from "react-toastify";
import postRatesToSave from "api/PostRatesToSave";
import fetchAnalyzedData from "api/FetchAnalyzedData";


interface SaveButtonProps {
  selectedCurrencies: string[];
  disabled: boolean
}

export const SaveButton: React.FC<SaveButtonProps> = ({ selectedCurrencies, disabled }) => {

  const postData = async () => {
    try {
      const response = await postRatesToSave(selectedCurrencies);

      if (response.status === 200) {
        toast.success(
          `Data for ${selectedCurrencies.join(', ')} successfully saved to the server! ✔️`,
          {theme: "dark"})
      } else {
        console.error("Failed to post data: ", response.status)
        toast.error(
          "Error occurred when saving data to the server ❌",
          {theme: "dark"})
      }
    } catch (error) {
      console.error("Error posting data: ", error)
    }
  };

  const fetchData = async () => {
    try {
      return await fetchAnalyzedData(selectedCurrencies);
    } catch (error) {
      console.error("Error fetching analyzed data:", error)
    }
  };

  const handleSavingClick = async () => {
    await postData();
    const analyzedData = await fetchData();

    for (const currencyPair in analyzedData) {
      const calculatedData = analyzedData[currencyPair]

      toast.info(
        <div><b>{currencyPair}</b> analyzed data<br />
          Average value: {calculatedData['average_value']}<br />
          Median value: {calculatedData['median_value']}<br />
          Min value: {calculatedData['min_value']}<br />
          Max value: {calculatedData['max_value']}<br />
        </div>,
        { position: "top-left", autoClose: false, draggable: false});
    }
  };

  return (
    <div>
      <button
        onClick={handleSavingClick}
        disabled={disabled}
        className={disabled ? "disabled" : "enabled"}
      >Save to server</button>
    </div>
  );
};

export default SaveButton;