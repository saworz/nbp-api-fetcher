import './CurrenciesRow.css';
import currencies from "../../../data/currencies";

const CurrenciesRow = ({currencyPair}) => {
  const getCountryCodeByCurrencyCode = (currencyCode) => {
    const currencyEntry = currencies.find((currency) => currency.currencyCode === currencyCode);

    if (currencyEntry) {
      return currencyEntry.countryCode;
    } else {
      console.error(`No matching currency entry found for currency code: ${currencyCode}`);
      return null;
    }
  };

  const [baseCurrency, targetCurrency] = currencyPair.split('/')
  const baseCountryCode = getCountryCodeByCurrencyCode(baseCurrency)
  const targetCountryCode = getCountryCodeByCurrencyCode(targetCurrency)

  return (
    <div>
      {currencyPair}
    </div>
  );
};

export default CurrenciesRow;