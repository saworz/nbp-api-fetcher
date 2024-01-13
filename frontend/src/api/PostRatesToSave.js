import axios from "axios";
import {toast} from "react-toastify";

export const postRatesToSave = async (currencyPairs) => {
  const requestData = JSON.stringify({ currency_pairs: currencyPairs})
  const requestUrl =  "http://127.0.0.1:5000/api/save_exchange_rates/"
  try {
    return await axios.post(requestUrl, requestData, {
      headers: {
      "Content-Type": "application/json",
      },
    })
  } catch (error) {
    console.error("Error posting data:", error)
    toast.error(
  "Failed to send data to the server ❌",
  {theme: "dark"})
  }
};

export default postRatesToSave;