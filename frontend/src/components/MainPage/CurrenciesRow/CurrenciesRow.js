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

  const getCountryFlagUrl = (countryCode) => {
    return `https://flagcdn.com/${countryCode}.svg`
  };

  const baseCountryFlagUrl = getCountryFlagUrl(baseCountryCode)
  const targetCountryFlagUrl = getCountryFlagUrl(targetCountryCode)

  console.log(baseCurrency, targetCurrency)
  console.log(baseCountryFlagUrl, targetCountryFlagUrl)
  return (
    <div>
      {currencyPair}
    </div>
  );
};

export default CurrenciesRow;