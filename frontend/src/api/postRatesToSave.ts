import axios from "axios";
import {toast} from "react-toastify";


interface ApiResponse {
  message: string;
  status: number;
}

export const postRatesToSave = async (currencyPairs: string[]): Promise<ApiResponse> => {
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
    toast.error("Failed to send data to the server ❌",
                {theme: "dark"})
    throw error;
  }
};

export default postRatesToSave;