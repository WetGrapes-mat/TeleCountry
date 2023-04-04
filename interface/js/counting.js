const button = document.querySelector('.counting__button');
setTimeout(function() {
    button.style.opacity = '1';
 }, 3200);
 button.style.transition = 'transition: 0.5s all';


const postData = async (url, data) => {
    let res = await fetch(url, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: data
    });

    return await res.json();
};

let resultObject = {};
button.addEventListener('click', () => {
    const active = document.querySelectorAll('.counting__pick.active');
    active.forEach(item => {
        resultObject[item.parentElement.id] = item.textContent;
    });
    const location = document.querySelector('.select__current');
    resultObject['location'] = location.textContent;
    let json = JSON.stringify(resultObject);
    postData('http://localhost:3000/requests', json);
});



