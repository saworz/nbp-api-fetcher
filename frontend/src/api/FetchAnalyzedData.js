import axios from "axios";
import {toast} from "react-toastify";

export const fetchAnalyzedData = async (selectedCurrencies) => {
  const apiUrl = "http://127.0.0.1:5000/api/analyze_data/";
  const queryParams = selectedCurrencies.map(query => `currencies=${query}`).join('&');
  const finalUrl = `${apiUrl}?${queryParams}`;

  try {
    const response = await axios.get(finalUrl);
    return response.data["analyzed_data"]
  } catch (error) {
    console.error("Error fetching data:", error)
    toast.error(
  "Failed to download currency pairs from the server ❌",
  {theme: "dark"})
  }
};

export default fetchAnalyzedData;