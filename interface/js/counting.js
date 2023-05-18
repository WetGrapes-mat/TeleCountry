const confirm = document.querySelector('.counting__button'),
   family = document.getElementById("family").getElementsByTagName("li"),
   kindergarten = document.getElementById("kindergarten").getElementsByTagName("li"),
   study = document.getElementById("school").getElementsByTagName("li"),
   cigs = document.getElementById("cigarettes").getElementsByTagName("li"),
   transport = document.getElementById("moving").getElementsByTagName("li"),
   rent = document.querySelector(".counting__select_current");

let prices = [];
document.getElementById("cigarettes").parentElement.style.width = '200px';
document.getElementById("moving").parentElement.style.width = '260px';
document.getElementById("school").parentElement.style.margin = '0 70px 0 0';

moving_picks = document.getElementById("moving").querySelectorAll('.counting__pick');
moving_picks.forEach((item, i) => {
    item.style.padding = '0 2px';
    if (i != 0){
         item.style.margin = '0 0 0 10px';
    }
    
});

setTimeout(function() {
      confirm.style.opacity = '1';
}, 3200);
confirm.style.transition = 'transition: 0.5s all';

async function getPrices(url, toPost) {
   try {
      const response = await fetch(url, {
         method: 'POST',
         body: JSON.stringify(toPost),
         headers: {
            'Content-Type': 'application/json'
         }
      });
      
      const res = await response.json();
      res.sort((a, b) => a.price - b.price);
      const slicedPrices = res.slice(0, 10);
      return slicedPrices;
   } catch (error) {
      console.error(error);
   }
 }
 
confirm.addEventListener('click', () => {
   let familyActiveElement, kindergartenActiveElement, schoolActiveElement, cigsActiveElement, movingActiveElement, locationActiveElement;
   for (let i = 0; i < family.length; i++) {
      if (family[i].classList.contains("active")) {
         familyActiveElement = family[i].textContent;
         break;
      }
   }
   for (let i = 0; i < kindergarten.length; i++) {
      if (kindergarten[i].classList.contains("active")) {
         kindergartenActiveElement = kindergarten[i].textContent;
         break;
      }
   }
   for (let i = 0; i < study.length; i++) {
      if (study[i].classList.contains("active")) {
         schoolActiveElement = study[i].textContent;
         break;
      }
   }
   for (let i = 0; i < cigs.length; i++) {
      if (cigs[i].classList.contains("active")) {
         cigsActiveElement = cigs[i].textContent;
         break;
      }
   }
   for (let i = 0; i < transport.length; i++) {
      if (transport[i].classList.contains("active")) {
         movingActiveElement = transport[i].textContent;
         break;
      }
   }
   if (location.textContent != 'Expand') {
      locationActiveElement = rent.textContent;
   }

   let data = {
      "family_member_amount": parseInt(familyActiveElement),
      "children_school": parseInt(schoolActiveElement),
      "children_preschool": parseInt(kindergartenActiveElement),
      "smoking_packs": parseInt(cigsActiveElement),
      "transportation": `${movingActiveElement}`,
      "rent": `${locationActiveElement}` 
   };
   getPrices('http://localhost:8080//cost_living', data)
      .then(prices => {
         const pricesStr = JSON.stringify(prices);
         const encodedStr = encodeURIComponent(pricesStr);
         window.location.assign(`../html/prices.html?prices=${encodedStr}`);
      })
});