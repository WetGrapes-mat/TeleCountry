window.addEventListener('DOMContentLoaded', function() {
    function makePickActive(parentID, index){
        let parent = document.querySelector(`#${parentID}`);
        let items = parent.querySelectorAll('.counting__pick');
        items.forEach((item) => {
            if (item.classList.contains('active')){
                item.classList.remove('active');
            }
            items[index].classList.add('active');
        });
    }


    let parents = document.querySelectorAll('.counting__picks');
    parents.forEach((parent) => {
        let picks = parent.querySelectorAll('.counting__pick');
        parent.addEventListener('click', function(event){
            const target = event.target;
            if (target && target.classList.contains('counting__pick')){
                picks.forEach((item, i) => {
                    if (target == item){
                        makePickActive(item.parentElement.id, i);
                    }
                });
            }
        });
    });
});