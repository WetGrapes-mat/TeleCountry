const gradients = {
    "css": {
        1: `<linearGradient id="gradient-1" x1="7%" y1="100%" x2="93%" y2="0%" >
                <stop offset="39%" style="stop-color:rgb(255,166,0);stop-opacity:1.00" />
                <stop offset="82%" style="stop-color:rgb(255,255,0);stop-opacity:1.00" />
            </linearGradient>\n`,
        2: `<linearGradient id="gradient-2" x1="0%" y1="50%" x2="100%" y2="50%" >
                <stop offset="35%" style="stop-color:rgb(255,250,29);stop-opacity:1.00" />
                <stop offset="100%" style="stop-color:rgb(10,163,17);stop-opacity:1.00" />
            </linearGradient>\n`,
        3: `<linearGradient id="gradient-3" x1="0%" y1="51%" x2="100%" y2="49%" >
                <stop offset="0%" style="stop-color:rgb(59,90,42);stop-opacity:1.00" />
                <stop offset="52%" style="stop-color:rgb(69,170,47);stop-opacity:1.00" />
                <stop offset="100%" style="stop-color:rgb(0,255,111);stop-opacity:1.00" />
            </linearGradient>\n`,
        4: `<linearGradient id="gradient-4" x1="0%" y1="50%" x2="100%" y2="50%" >
                <stop offset="35%" style="stop-color:rgb(29,255,253);stop-opacity:1.00" />
                <stop offset="100%" style="stop-color:rgb(12,10,163);stop-opacity:1.00" />
            </linearGradient>\n`,
        5: `<linearGradient id="gradient-5" x1="0%" y1="51%" x2="100%" y2="49%" >
                <stop offset="0%" style="stop-color:rgb(18,12,63);stop-opacity:1.00" />
                <stop offset="51%" style="stop-color:rgb(27,23,110);stop-opacity:1.00" />
                <stop offset="100%" style="stop-color:rgb(27,113,210);stop-opacity:1.00" />
            </linearGradient>\n`,
        6: `<linearGradient id="gradient-6" x1="0%" y1="50%" x2="100%" y2="50%" >
                <stop offset="28%" style="stop-color:rgb(222,238,130);stop-opacity:1.00" />
                <stop offset="100%" style="stop-color:rgb(0,183,255);stop-opacity:1.00" />
            </linearGradient>\n`,
        7: `<linearGradient id="gradient-7" x1="0%" y1="50%" x2="100%" y2="50%" >
                <stop offset="0%" style="stop-color:rgb(128,32,0);stop-opacity:1.00" />
                <stop offset="100%" style="stop-color:rgb(238,130,238);stop-opacity:1.00" />
            </linearGradient>\n`,
        8: `<linearGradient id="gradient-8" x1="0%" y1="50%" x2="100%" y2="50%" >
                <stop offset="10%" style="stop-color:rgb(238,130,238);stop-opacity:1.00" />
                <stop offset="52%" style="stop-color:rgb(154,30,180);stop-opacity:1.00" />
                <stop offset="100%" style="stop-color:rgb(0,209,255);stop-opacity:1.00" />
            </linearGradient>\n`,
        9: `<linearGradient id="gradient-9" x1="0%" y1="50%" x2="100%" y2="50%" >
                <stop offset="13%" style="stop-color:rgb(163,65,65);stop-opacity:1.00" />
                <stop offset="47%" style="stop-color:rgb(255,204,38);stop-opacity:1.00" />
                <stop offset="87%" style="stop-color:rgb(159,170,36);stop-opacity:1.00" />
            </linearGradient>\n`,
        10: `<linearGradient id="gradient-10" x1="89%" y1="0%" x2="11%" y2="100%" >
                <stop offset="14%" style="stop-color:rgb(157,65,65);stop-opacity:1.00" />
                <stop offset="55%" style="stop-color:rgb(242,38,255);stop-opacity:1.00" />
                <stop offset="84%" style="stop-color:rgb(120,31,147);stop-opacity:1.00" />
            </linearGradient>\n`
    },
    "svg": {
        1: 'linear-gradient(-49.3deg, rgb(255, 166, 0) 39%, rgb(255, 255, 0) 82%)',
        2: 'linear-gradient(90deg, rgb(255, 250, 29) 35%, rgb(10, 163, 17) 100%)',
        3: 'linear-gradient(-1.15deg, rgb(59, 90, 42) 0%, rgb(69, 170, 47) 52%, rgb(0, 255, 111) 100%)',
        4: 'linear-gradient(90deg, rgb(29, 255, 253) 35%, rgb(12, 10, 163) 100%)',
        5: 'linear-gradient(-1.15deg, rgb(18, 12, 63) 0%, rgb(27, 23, 110) 51%, rgb(27, 113, 210) 100%)',
        6: 'linear-gradient(90deg, rgb(222, 238, 130) 28%, rgb(0, 183, 255) 100%)',
        7: 'linear-gradient(90deg, rgb(128, 32, 0) 0%, rgb(238, 130, 238) 100%)',
        8: 'linear-gradient(90deg, rgb(238, 130, 238) 10%, rgb(154, 30, 180) 52%, rgb(0, 209, 255) 100%)',
        9: 'linear-gradient(90deg, rgb(163, 65, 65) 13%, rgb(255, 204, 38) 47%, rgb(159, 170, 36) 87%)',
        10: 'linear-gradient(-52.05deg, rgb(157, 65, 65) 14%, rgb(242, 38, 255) 55%, rgb(120, 31, 147) 84%)'
    }
};

let lifeDB = [];
const lifePageSize = 10;

async function getLife(url) {
    try {
        const response = await fetch(url);
        const data = await response.json();
        lifeDB = data;
        addCountryElements(lifeDB, 0, 10);
    } catch (error) {
        console.error(error);
    }
}

getLife('http://localhost:8080///standard_of_living');

const lifePrevButton = document.querySelector('#life-prev'),
    lifeNextButton = document.querySelector('#life-next'),
    lifeCurrentPage = document.querySelector('#life-current'),
    lifeTotalElement = document.querySelector('#life-total'),
    lifeWrapper = document.querySelector('.stats__countries'),
    diagram = document.querySelector('.stats__diagram');

lifePrevButton.addEventListener('click', goToPreviousPage);
lifeNextButton.addEventListener('click', goToNextPage);

function goToPreviousPage() {
    const currentPageNumber = parseInt(lifeCurrentPage.textContent);
    if (currentPageNumber > 1) {
        const previousPageNumber = currentPageNumber - 1;
        lifeCurrentPage.textContent = previousPageNumber;

        const startIndex = (previousPageNumber - 1) * lifePageSize;
        const endIndex = startIndex + lifePageSize;

        lifeWrapper.innerHTML = '';
        addCountryElements(lifeDB.slice(startIndex, endIndex));
    }
}
  
function goToNextPage() {
    const currentPageNumber = parseInt(lifeCurrentPage.textContent);
    const totalPageNumber = parseInt(lifeTotalElement.textContent);
    if (currentPageNumber < totalPageNumber) {
        const nextPageNumber = currentPageNumber + 1;
        lifeCurrentPage.textContent = nextPageNumber;

        const startIndex = (nextPageNumber - 1) * lifePageSize;
        const endIndex = startIndex + lifePageSize;

        lifeWrapper.innerHTML = '';
        addCountryElements(lifeDB.slice(startIndex, endIndex));
    }
}

function addCountryElements(data, startIndex, endIndex) {
    const lifePagesTotal = Math.ceil(lifeDB.length / lifePageSize);
    lifeTotalElement.textContent = lifePagesTotal;
    diagram.innerHTML= '';
    x_center = 265
    y_center = 209
    let diagram_content = '<defs>\n';
    for (let i = 1; i < 11; i++)
    {
        diagram_content += `${gradients["css"][i]}`;
    }
    diagram_content += '</defs>\n';
    for (let i = 0; i < 10; i++)
    {
        let radius = 25 + 20 * i;
        diagram_content += `<circle class="stats__diagram_back animate__animated animate__fadeIn wow" cx="${x_center}" cy="${y_center}" r="${radius}" stroke="rgb(25, 25, 25)" id="circle-${i+1}-back"/>\n`;
    }
    data.slice(startIndex, endIndex).forEach((obj, i) => {
        let country = obj.country;
        if (country === 'United Kingdom') {
            country = 'UK';
        } else if (country === 'United States of America') 
        {
            country = 'USA';
        } else if (country === 'United Arab Emirates') {
            country = 'UAE';
        }
        const level = obj.level;
        console.log(typeof(level));
        
        const countryElement = document.createElement('div');
        countryElement.classList.add('stats__country', 'animate__animated', 'animate__fadeInRight', 'wow');
        
        const countryBlock = document.createElement('div');
        countryBlock.classList.add('stats__country_block');
        
        const countryColor = document.createElement('div');
        countryColor.classList.add('stats__country_color');
        
        const countryName = document.createElement('div');
        countryName.textContent = country;
        countryName.classList.add('stats__country_name');
        
        const countryLevel = document.createElement('div');
        countryLevel.textContent = level;
        countryLevel.classList.add('stats__country_level');
        
        countryBlock.appendChild(countryColor);
        countryBlock.appendChild(countryName);
        
        countryElement.appendChild(countryBlock);
        countryElement.appendChild(countryLevel);

        let radius = 25 + 20 * i;
        let length = Math.floor(2 * 3.14 * radius);
        let procent = Math.floor(length * level / 100);
        diagram_content += `<circle class="stats__diagram_front animate__animated animate__fadeIn wow" cx="${x_center}" cy="${y_center}" r="${radius}" stroke-dasharray="${procent} ${length - procent}" stroke-dashoffset="${-(length / 4)}" stroke="url(#gradient-${i+1})" id="circle-${i+1}-front"/>\n`;

        lifeWrapper.appendChild(countryElement);
    });
    diagram.innerHTML= diagram_content;
    let countries_colors = document.querySelectorAll('.stats__country_color');
    countries_colors.forEach((element, index) => {
        element.style.background = gradients["svg"][index + 1];
    });
}


  