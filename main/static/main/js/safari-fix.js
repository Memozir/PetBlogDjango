'use strict'

// window.addEventListener('resize', () => {
//     let vh = window.innerHeight * 0.01;
//     document.documentElement.style.setProperty('--vh', `${vh}px`);
//   });

  window.onresize = function(){
    document.body.height = window.innerHeight;
  }
  window.onresize()