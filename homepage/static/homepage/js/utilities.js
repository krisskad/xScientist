const header = document.getElementsByTagName("header")[0];
const body = document.getElementById("body");
const loader = document.getElementById("loader");
function toggleHeader(){
  header.classList.toggle("close");
}

window.onload = function(){
  setTimeout(function(){
    console.log("loaded");
    body.classList.toggle("d_none");
    loader.classList.toggle("d_none");
  },1000);
}

const swiper = new Swiper('.swiper', {
  slidesPerView: 2,
  spaceBetween: 0,
  pagination: {
    el: '.swiper-pagination',
    type: 'bullets',
    clickable:true,
  },
  autoplay: {
    delay: 2500,
    disableOnInteraction: false
  },
  speed: 1500,
  grabCursor: true,
  mousewheelControl: true,
  centeredSlides: true,
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  breakpoints: {
    '600': {
      slidesPerView: 2,
      spaceBetween: 20,
    },
    '768': {
      slidesPerView: 3,
      spaceBetween: 40,
    },
    '992': {
      slidesPerView: 4,
      spaceBetween: 50,
    },
    '1200': {
      slidesPerView: 4,
      spaceBetween: 50,
    },
  }
});