'use strict'

const formShowBtn = document.querySelector('.block-first__button');
const formCloseBtn = document.querySelector('.form__close_button');
const form = document.querySelector('.questions-wrap');

formShowBtn.addEventListener('click', e => {
    form.classList.add('display_form');
 });

formCloseBtn.addEventListener('click', e => {
    form.classList.remove('display_form');
 });

const submitButton = document.querySelector('.questions-form__button');
const filteringElements = document.querySelectorAll('.filter');

submitButton.addEventListener('click', e => {
      filteringElements.forEach(element => {
          element.style.display = 'none';
          form.classList.remove('display_form');
      });
});

