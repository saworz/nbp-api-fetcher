import "./SaveButton.css"
import postRatesToSave from "../../../api/PostRatesToSave";

export const SaveButton = ({ selectedCurrencies }) => {
  const postData = async () => {
    try {
      await postRatesToSave(selectedCurrencies);
    } catch (error) {
      console.error("Error fetching exchange rates:", error)
    }
  };
  const handleSavingClick = async () => {
    await postData();
  };

  return (
    <div>
      <button onClick={handleSavingClick}>Save to server</button>
    </div>
  );
};

export default SaveButton;