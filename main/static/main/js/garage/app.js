

// SLIDER -- START
document.addEventListener('DOMContentLoaded', function() {
    const prevBtn = document.querySelector('.prev');
    const nextBtn = document.querySelector('.next');
    const slidesContainer = document.querySelector('.slides');

    prevBtn.addEventListener('click', function(e) {
      
      e.preventDefault();
      slidesContainer.scrollBy({
        left: -100,
        behavior: 'smooth'
      });
    });
  
    nextBtn.addEventListener('click', function(e) {
      
      e.preventDefault();
      slidesContainer.scrollBy({
        left: 1000,
        behavior: 'smooth'
      });
    });
});
// SLIDER -- END 




// // SELL MENU -- START
// const sell_btns = document.getElementsByClassName("sell_btn")
// const sell_menu = document.getElementById("sell_menu")

// var sellButtons = document.getElementsByClassName('sell_btn');

// Array.from(sellButtons).forEach(function(button) {
//   button.addEventListener('click', function() {
//     sell_menu.style.display = "flex"
//   });
// });
// // SELL MENU -- END
