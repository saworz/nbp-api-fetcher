import "./DownloadButton.css"
import { useState, useEffect } from "react";
import fetchExchangeRates from "../../../api/FetchExchangeRates";

export const DownloadButton = ({ selectedCurrencies }) => {
  const [exchangeRates, setExchangeRates] = useState();

  const downloadExchangeRatesAsCSV = () => {
    const csvData = [];
    for (const currency in exchangeRates) {
      const rates = exchangeRates[currency];
      const rowData = { Date: currency };

      for (const date in rates) {
        rowData[date] = rates[date];
      }

      csvData.push(rowData);
    }

    const csvContent = Object.keys(csvData[0]).map(key => key + ',' + csvData.map(row => row[key]).join(',')).join('\n');
    const blob = new Blob([csvContent], { type: "text/csv" });
    const link = document.createElement("a");
    link.href = window.URL.createObjectURL(blob);
    link.download = "exchangeRates.csv";

    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  useEffect(() => {
    if (exchangeRates) {
      downloadExchangeRatesAsCSV()
    }
  }, [exchangeRates]);

  const fetchData = async () => {
    try {
      const data = await fetchExchangeRates(selectedCurrencies);
      setExchangeRates(data);
    } catch (error) {
      console.error("Error fetching exchange rates:", error)
    }
  };

  const handlePreviewClick = async () => {
    await fetchData();
  };

  return (
    <div>
      <button onClick={handlePreviewClick}>Download as .CSV</button>
    </div>
  );
};

export default DownloadButton;