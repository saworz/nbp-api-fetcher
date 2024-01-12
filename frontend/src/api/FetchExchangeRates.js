import axios from "axios";

export const fetchExchangeRates = async () => {
  try {
    const response = await axios.get("http://127.0.0.1:5000/api/get_exchange_rates/?currencies=USD/PLN&currencies=EUR/PLN");
    return response.data
  } catch (error) {
    console.error("Error fetching data:", error)
  }
};

export default fetchExchangeRates;