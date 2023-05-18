const dangerWrapper = document.querySelector('.stats__danger');
let dangerDB = [];
const dangerPageSize = 16;

async function getDanger(url) {
    try {
        const response = await fetch(url);
        const data = await response.json();
        dangerDB = data;
        createDangerElements(dangerDB, 0, dangerPageSize);
    } catch (error) {
        console.error(error);
    }
}

getDanger('http://localhost:8080//most_dangerous_places');

const dangerPrevButton = document.querySelector('#stats-prev'),
    dangerNextButton = document.querySelector('#stats-next'),
    dangerCurrentPage = document.querySelector('#danger-current'),
    dangerTotalElement = document.querySelector('#danger-total');

dangerPrevButton.addEventListener('click', goToPreviousPage);
dangerNextButton.addEventListener('click', goToNextPage);

function goToPreviousPage() {
    const currentPageNumber = parseInt(dangerCurrentPage.textContent);
    if (currentPageNumber > 1) {
        const previousPageNumber = currentPageNumber - 1;
        dangerCurrentPage.textContent = previousPageNumber;

        const startIndex = (previousPageNumber - 1) * dangerPageSize;
        const endIndex = startIndex + dangerPageSize;

        dangerWrapper.innerHTML = '';
        createDangerElements(dangerDB.slice(startIndex, endIndex));
    }
    
    return false;
}
  
function goToNextPage() {
    const currentPageNumber = parseInt(dangerCurrentPage.textContent);
    const totalPageNumber = parseInt(dangerTotalElement.textContent);
    if (currentPageNumber < totalPageNumber) {
        const nextPageNumber = currentPageNumber + 1;
        dangerCurrentPage.textContent = nextPageNumber;

        const startIndex = (nextPageNumber - 1) * dangerPageSize;
        const endIndex = startIndex + dangerPageSize;

        dangerWrapper.innerHTML = '';
        createDangerElements(dangerDB.slice(startIndex, endIndex));
    }
    
    return false;
}

function createDangerElements(data, startIndex, endIndex) {
    const dangerPagesTotal = Math.ceil(dangerDB.length / dangerPageSize);
    dangerTotalElement.textContent = dangerPagesTotal;
    data.slice(startIndex, endIndex).forEach(obj => {
        const country = obj.country;
        const hr = obj.hr;
        const cta = obj.cta;
        const sa = obj.sa;
    
        const dangerElement = document.createElement('div');
        dangerElement.classList.add('stats__danger_element', 'animate__animated', 'animate__fadeInLeft', 'wow');
    
        const dangerWrap = document.createElement('div');
        dangerWrap.classList.add('stats__danger_wrap');
    
        const flagImg = document.createElement('img');
        flagImg.src = `../img/flags/${country.replace(/\s+/g, '_').toLowerCase()}.png`;
        flagImg.alt = country;
        flagImg.classList.add('stats__danger_img');
    
        const countryName = document.createElement('div');
        countryName.textContent = country;
        countryName.classList.add('stats__danger_name');
    
        const hrValue = document.createElement('div');
        hrValue.textContent = hr.toFixed(3);
        hrValue.classList.add('stats__danger_hr');
    
        const ctaValue = document.createElement('div');
        ctaValue.textContent = cta.toFixed(3);
        ctaValue.classList.add('stats__danger_cta');
    
        const saValue = document.createElement('div');
        saValue.textContent = sa.toFixed(3);
        saValue.classList.add('stats__danger_sa');
    
        dangerWrap.appendChild(flagImg);
        dangerWrap.appendChild(countryName);
    
        dangerElement.appendChild(dangerWrap);
        dangerElement.appendChild(hrValue);
        dangerElement.appendChild(ctaValue);
        dangerElement.appendChild(saValue);
    
        dangerWrapper.appendChild(dangerElement);
    });
}

createDangerElements(dangerDB, 0, 15);


  