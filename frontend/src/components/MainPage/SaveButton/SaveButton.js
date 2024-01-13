import "./SaveButton.css"
import postRatesToSave from "../../../api/PostRatesToSave";
import { useState, useEffect } from "react";

export const SaveButton = ({ selectedCurrencies, onSuccessfulSave, disabled }) => {
  const [saveSuccess, setSaveSuccess] = useState(false);
  const postData = async () => {
    try {
      const response = await postRatesToSave(selectedCurrencies);

      if (response.status === 200) {
        setSaveSuccess(true)
      } else {
        console.error("Failed to post data: ", response.status)
      }
    } catch (error) {
      console.error("Error posting data: ", error)
    }
  };

  useEffect((onSuccessfulSave) => {
    if (saveSuccess) {
      onSuccessfulSave()
      setTimeout(() => {
        setSaveSuccess(false);
        console.log("setting to false")
      }, 5000);
    }
  }, [saveSuccess]);

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