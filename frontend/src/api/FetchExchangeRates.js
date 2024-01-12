import axios from "axios";

export const fetchExchangeRates = async (selectedCurrencies) => {
  const apiUrl = "http://127.0.0.1:5000/api/get_exchange_rates/";
  const queryParams = selectedCurrencies.map(query => `currencies=${query}`).join('&');
  const finalUrl = `${apiUrl}?${queryParams}`;

  try {
    const response = await axios.get(finalUrl);
    const jsonValidString = response.data.replace(/:\s*NaN/g, ": null");
    return JSON.parse(jsonValidString)["exchange_rates"];
  } catch (error) {
    console.error("Error fetching data:", error)
  }
};

export default fetchExchangeRates;