import "./DownloadButton.css"
import { useState, useEffect } from "react";
import fetchExchangeRates from "../../../api/FetchExchangeRates";
import { toast } from "react-toastify";

export const DownloadButton = ({ selectedCurrencies, disabled }) => {
  const [exchangeRates, setExchangeRates] = useState();

  useEffect(() => {
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

    if (exchangeRates) {
      try {
        downloadExchangeRatesAsCSV()
      } catch {
        toast.error(
          "Failed to convert data to .csv ❌",
          {theme: "dark"})
      }

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
      <button
        onClick={handlePreviewClick}
        disabled={disabled}
        className={disabled ? "disabled" : "enabled"}
      >Download as .csv</button>
    </div>
  );
};

export default DownloadButton;