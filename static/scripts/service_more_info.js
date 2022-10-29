'use strict'

const services = document.querySelectorAll('.service');

services.forEach(element => {
    const moreInfoButton = element.querySelector('.service a');
    const moreInfoBlock = element.querySelector('.service__more-info__block');

    moreInfoButton.addEventListener('click', e =>{
        moreInfoBlock.classList.toggle('service__more-info__block_visible');
    });

});