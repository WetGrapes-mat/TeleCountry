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
