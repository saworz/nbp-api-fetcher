import "./DownloadButton.css";
import { toast } from "react-toastify";
import { useState, useEffect, SetStateAction } from "react";
import fetchExchangeRates from "api/fetchExchangeRates";

interface DownloadButtonProps {
  selectedCurrencies: string[];
  disabled: boolean;
}

interface IExchangeRates {
  [currencyPair: string]: {
    [date: string]: number | null;
  };
}

export const DownloadButton: React.FC<DownloadButtonProps> = ({
  selectedCurrencies,
  disabled,
}) => {
  const [exchangeRates, setExchangeRates] = useState<IExchangeRates>();

  useEffect(() => {
    const downloadExchangeRatesAsCSV = () => {
      const datesColumn: { Date: string }[] = [];

      for (const currency in exchangeRates) {
        const rates = exchangeRates[currency];
        const rowData: { Date: string; [key: string]: any } = {
          Date: currency,
        };

        for (const date in rates) {
          rowData[date] = rates[date];
        }

        datesColumn.push(rowData);
      }

      const csvContent = Object.keys(datesColumn[0])
        .map(
          (key) =>
            key + "," + datesColumn.map((row) => (row as any)[key]).join(",")
        )
        .join("\n");
      const blob = new Blob([csvContent], { type: "text/csv" });
      const link = document.createElement("a");
      link.href = window.URL.createObjectURL(blob);
      link.download = "selected_currency_data.csv";

      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    };

    if (exchangeRates) {
      try {
        downloadExchangeRatesAsCSV();
      } catch {
        toast.error("Failed to convert data to .csv ❌", { theme: "dark" });
      }
    }
  }, [exchangeRates]);

  const fetchData = async () => {
    try {
      const data = (await fetchExchangeRates(
        selectedCurrencies
      )) as SetStateAction<any>;
      setExchangeRates(data);
    } catch (error) {
      console.error("Error fetching exchange rates:", error);
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
      >
        Download as .csv
      </button>
    </div>
  );
};

export default DownloadButton;
