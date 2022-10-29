'use strict'

window.onload = function(){
    const showAllButton = document.querySelector('.service__show-more');
    const showElements = document.querySelector('.services_second');

    showAllButton.addEventListener('click', e => {
        showElements.classList.toggle('services_show_more');
    });
};