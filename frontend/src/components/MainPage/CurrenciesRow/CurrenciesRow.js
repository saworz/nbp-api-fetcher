import './CurrenciesRow.css';

const CurrenciesRow = ({currencyPair}) => {
  const [baseCurrency, targetCurrency] = currencyPair.split('/')
  console.log(baseCurrency, targetCurrency)
  return (
    <div>
      {currencyPair}
    </div>
  );
};

export default CurrenciesRow;