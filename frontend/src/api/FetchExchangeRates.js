import axios from "axios";

export const fetchExchangeRates = async (selectedCurrencies) => {
  console.log("IN fetching")
  console.log(selectedCurrencies)
  const apiUrl = "http://127.0.0.1:5000/api/get_exchange_rates/";
  const queryParams = selectedCurrencies.map(query => `currencies=${query}`).join('&');
  const finalUrl = `${apiUrl}?${queryParams}`;

  console.log(finalUrl)
  try {
    const response = await axios.get(finalUrl);
    return response.data
  } catch (error) {
    console.error("Error fetching data:", error)
  }
};

export default fetchExchangeRates;