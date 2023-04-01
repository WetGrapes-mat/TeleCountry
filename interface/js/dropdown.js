let cigarettes = document.querySelector('#cigarettes'),
    moving = document.querySelector('#moving'),
    school = document.querySelector('#school');

cigarettes.parentElement.style.width = '152px';
moving.parentElement.style.width = '260px';
school.parentElement.style.margin = '0 70px 0 0';

moving_picks = moving.querySelectorAll('.counting__pick');
moving_picks.forEach((item, i) => {
    item.style.padding = '0 2px';
    if (i != 0){
        item.style.margin = '0 0 0 10px';
    }
    
});

let header = document.querySelector('.counting__select_header'),
    body = document.querySelector('.counting__select_body'),
    image = document.querySelector('.counting__select_icon img'),
    items = body.querySelectorAll('.counting__select_item'),
    current = header.querySelector('.counting__select_current');


function makeMenuUnactive(){
    body.classList.remove('active');
    header.classList.remove('active');
    image.src = '../img/price/down.png';
}

function makeMenuActive(){
    body.classList.add('active');
    header.classList.add('active');
    image.src = '../img/price/up.png';
}

header.addEventListener('click', function(){
    if (body.classList.contains('active')){
        makeMenuUnactive();
    } else{
        makeMenuActive();
    }
});

items.forEach(item => {
    item.addEventListener('click', function() {
        makeMenuUnactive();
        current.textContent = item.textContent;
    });
});