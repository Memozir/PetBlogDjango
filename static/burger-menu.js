'use strict'

window.onload = function(){

    const menuIcon = document.querySelector('.menu__icon');
    const menu = document.querySelector('.header__list');
    const body = document.querySelector('body');
    const header = document.querySelector('.header');

    menuIcon.addEventListener("click", e => {
        // const headerHeight = header.getBoundingClientRect().height
        // let pageScroll = document.scrollTop
        // menu.style.top = headerHeight + pageScroll + "px";
        // window.scrollBy(0, headerHeight);
    
        menu.classList.toggle('burger-menu-click');
        body.classList.toggle('body-overflow');
        header.classList.toggle('header_fixed');
        menuIcon.classList.toggle('_active');
    });

    let burgerScrollItems = document.querySelectorAll('a.burger-scroll-item');

    burgerScrollItems.forEach(element => {
        element.addEventListener("click", e => {
            menu.classList.remove('burger-menu-click');
            body.classList.remove('body-overflow');
            header.classList.remove('header_fixed');
            menuIcon.classList.remove('_active');
        })
    });

    // document.addEventListener("scroll", e => {
    //     const headerHeight = header.getBoundingClientRect().height
    //     let pageScroll = document.scrollTop
    //     menu.style.top = headerHeight + pageScroll + "px";
    //     console.log('MENU POSITION IS APPLIED');
    // })
}

