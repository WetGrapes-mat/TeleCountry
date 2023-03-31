let header = document.querySelector('.counting__select_header'),
    body = document.querySelector('.counting__select_body'),
    image = document.querySelector('.counting__select_icon img'),
    items = body.querySelectorAll('.counting__select_item'),
    current = header.querySelector('.counting__select_current');


function makeMenuUnactive(){
    body.classList.remove('active');
    header.classList.remove('active');
    image.src = 'img/price/down.png';
}

function makeMenuActive(){
    body.classList.add('active');
    header.classList.add('active');
    image.src = 'img/price/up.png';
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