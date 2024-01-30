import axios from "axios";
import {toast} from "react-toastify";

interface ApiResponse {
  string: {
    string: number | null
  }
}

export const fetchExchangeRates = async (selectedCurrencies: string[]): Promise<ApiResponse> => {
  const apiUrl = "http://127.0.0.1:5000/api/get_exchange_rates/";
  const queryParams = selectedCurrencies.map(query => `currencies=${query}`).join('&');
  const finalUrl = `${apiUrl}?${queryParams}`;

  try {
    const response = await axios.get(finalUrl);
    return response.data["exchange_rates"]
  } catch (error) {
    console.error("Error fetching data:", error)
    toast.error("Failed to download analyzed data from the server ❌",
                {theme: "dark"})
    throw error;
  }
};

export default fetchExchangeRates;