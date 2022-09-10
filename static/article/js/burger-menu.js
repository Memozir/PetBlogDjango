'use strict'

window.onload = function(){

    const menuIcon = document.querySelector('.menu__icon')
    

    menuIcon.addEventListener("click", e => {
    
        const menu = document.querySelector('.header__list')
        const body = document.querySelector('body')
        const header = document.querySelector('.header')
    
        menu.classList.toggle('burger-menu-click')
        body.classList.toggle('body-overflow')
        header.classList.toggle('header_fixed')
        menuIcon.classList.toggle('_active')
    
        const headerHeight = header.getBoundingClientRect().height
        menu.style.top = headerHeight - body.scrollTop + "px";
    });
}

