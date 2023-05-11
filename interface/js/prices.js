const pricesWrapper = document.querySelector('.price__wrapper');

const urlParams = new URLSearchParams(window.location.search);
const encodedParams = urlParams.get('prices');

// Раскодируйте полученную строку и преобразуйте обратно в объект
const decodedParams = decodeURIComponent(encodedParams);
const pricesDB = JSON.parse(decodedParams);

pricesDB.forEach((item, index) => {
    const country = item.country;
    let formattedCountry = country;

    if (country === 'United Kingdom') {
        formattedCountry = 'UK';
    } else if (country === 'United States of America') {
        formattedCountry = 'USA';
    } else if (country === 'United Arab Emirates') {
        formattedCountry = 'UAE';
    }

    const priceElement = document.createElement('div');
    priceElement.classList.add('price__country', 'animate__animated', 'animate__fadeInLeft', 'wow');

    const numberElement = document.createElement('div');
    numberElement.classList.add('price__number');
    numberElement.textContent = index + 1;

    const flagElement = document.createElement('img');
    flagElement.src = `../img/flags/${formattedCountry.toLowerCase()}.png`;
    flagElement.alt = formattedCountry;
    flagElement.classList.add('price__flag');

    const titlesElement = document.createElement('div');
    titlesElement.classList.add('price__titles');

    const nameElement = document.createElement('div');
    nameElement.classList.add('price__name');
    nameElement.textContent = formattedCountry;

    const costElement = document.createElement('div');
    costElement.classList.add('price__cost');
    costElement.textContent = `$${item.price.toFixed(2)}`;

    titlesElement.appendChild(nameElement);
    titlesElement.appendChild(costElement);

    priceElement.appendChild(numberElement);
    priceElement.appendChild(flagElement);
    priceElement.appendChild(titlesElement);

    pricesWrapper.appendChild(priceElement);
});
  