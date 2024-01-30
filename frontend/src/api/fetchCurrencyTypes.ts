import axios from "axios";
import { toast } from "react-toastify";

export const fetchCurrencyTypes = async () => {
  const requestUrl = "http://127.0.0.1:5000/api/get_currency_types";
  try {
    const response = await axios.get(requestUrl);
    return response.data["currencies_list"];
  } catch (error) {
    console.error("Error fetching data:", error);
    toast.error("Failed to download currency pairs from the server ❌", {
      theme: "dark",
    });
  }
};

export default fetchCurrencyTypes;
