import "./CurrencyRow.css";
import currencies from "data/currencies";

interface ICurrencyPair {
  currencyPair: string;
}

const CurrencyRow: React.FC<ICurrencyPair> = ({ currencyPair }) => {
  const getCountryCodeByCurrencyCode = (currencyCode: string) => {
    const currencyEntry = currencies.find(
      (currency) => currency.currencyCode === currencyCode
    );

    if (currencyEntry) {
      return currencyEntry.countryCode;
    } else {
      console.error(
        `No matching currency entry found for currency code: ${currencyCode}`
      );
      return undefined;
    }
  };

  const [baseCurrency, targetCurrency] = currencyPair.split("/");
  const baseCountryCode = getCountryCodeByCurrencyCode(baseCurrency);
  const targetCountryCode = getCountryCodeByCurrencyCode(targetCurrency);

  const getCountryFlagUrl = (countryCode: string) => {
    return `https://flagcdn.com/${countryCode}.svg`;
  };

  let baseCountryFlagUrl;
  let targetCountryFlagUrl;

  if (baseCountryCode) {
    baseCountryFlagUrl = getCountryFlagUrl(baseCountryCode);
  }

  if (targetCountryCode) {
    targetCountryFlagUrl = getCountryFlagUrl(targetCountryCode);
  }

  return (
    <div className="flags">
      {baseCountryFlagUrl && (
        <img src={baseCountryFlagUrl} alt={baseCountryCode} />
      )}
      <div className="exchange-text">
        {baseCurrency} &rarr; {targetCurrency}
      </div>
      {targetCountryFlagUrl && (
        <img src={targetCountryFlagUrl} alt={targetCountryCode} />
      )}
    </div>
  );
};

export default CurrencyRow;
