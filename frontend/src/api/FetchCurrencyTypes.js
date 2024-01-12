import axios from "axios";

export const fetchCurrencyTypes = async () => {
  const request_url = "http://127.0.0.1:5000/api/get_currency_types"
  try {
    const response = await axios.get(request_url);
    return response.data['currencies_list']
  } catch (error) {
    console.error("Error fetching data:", error)
  }
};

export default fetchCurrencyTypes;