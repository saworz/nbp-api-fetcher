import "./SaveButton.css"
import postRatesToSave from "../../../api/PostRatesToSave";
import { toast } from "react-toastify";

export const SaveButton = ({ selectedCurrencies, disabled }) => {

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

  const handleSavingClick = async () => {
    await postData();
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