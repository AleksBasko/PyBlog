/**
 * Created by user0 on 29.09.2017.
 */
(function () {
    console.log('first');
    showMenu();
}());

function showMenu() {
    let btn = document.getElementById('menu-btn');
    let menu = document.getElementById('menu-block');
    let itemList = menu.querySelectorAll('.menu__item');

    btn.addEventListener('click', function() {
        console.log(itemList);
        for(let i=0; i < itemList.length; i++) {
            setTimeout(function(){
                itemList[i].classList.add('active');
            }, i * 1000);
        }
    })
}