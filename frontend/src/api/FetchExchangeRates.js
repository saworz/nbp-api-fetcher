import axios from "axios";

export const fetchExchangeRates = async () => {
  const request_url = "http://127.0.0.1:5000/api/get_exchange_rates/?currencies=USD/PLN&currencies=EUR/PLN"
  try {
    const response = await axios.get(request_url);
    return response.data
  } catch (error) {
    console.error("Error fetching data:", error)
  }
};

export default fetchExchangeRates;