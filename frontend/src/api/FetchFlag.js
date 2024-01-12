export const fetchFlag = async () => {
  try {
    const response = await fetch(`https://flagcdn.com/${countryIso}.svg`);

    if (response.ok) {
      setFlagUrl(response.url);
    } else {
      console.error(`Failed to fetch flag for ${countryIso}. Status: ${response.status}`);
    }
  } catch (error) {
    console.error('Error fetching flag:', error);
  }
};

export default fetchFlag();