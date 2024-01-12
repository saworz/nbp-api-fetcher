export const fetchCurrencyTypes = async () => {
  try {
    const response = await fetch("http://localhost:8000/api/get_currency_types");
    if (response.ok) {
      return await response.json();
    } else {
      console.error("Failed to fetch the data")
    }
  } catch (error) {
    console.error("Error fetching data:", error)
  }
};

export default fetchCurrencyTypes;