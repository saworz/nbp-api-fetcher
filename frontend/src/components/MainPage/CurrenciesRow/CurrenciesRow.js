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

  return (
    <div className="flags">
      {baseCountryFlagUrl && (
        <img src={baseCountryFlagUrl} alt={baseCountryCode}/>
      )}
      <div className="exchange-text">
        {baseCurrency} -> {targetCurrency}
      </div>
      {targetCountryFlagUrl && (
        <img src={targetCountryFlagUrl} alt={targetCountryCode}/>
      )}
    </div>
  );
};

export default CurrenciesRow;