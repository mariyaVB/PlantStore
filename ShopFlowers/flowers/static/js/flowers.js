//Карусель flower.html
let assortment = $('.assortment'),
    list_assortment = $('.list-assortment'),
    countAssortment = assortment.length,
    position = 0,
    step = 150;
    max = (countAssortment * 150) - 900;

$(list_assortment).width(150 * countAssortment);
$('.next').click(function () {
    if (position == -max) {
        position = 0;
        list_assortment.css("left", position + "px");
    }else{
        position = position - step;
        list_assortment.css("left", position + "px");
    }
});

$('.prev').click(function () {
    if (position == 0) {
        position = -max;
        list_assortment.css("left", position + "px");
    }else{
        position = position + step;
        list_assortment.css("left", position + "px");
    }
});


// Показать скрыть отзывы 
let alreadyScrolled = false; // Флаг для отслеживания прокрутки

$('.feedback-count-rating-mean').click(function() {
  $('.feedback-list').toggle(); 

  // Прокрутка только если ещё не прокручивали
  if (!alreadyScrolled) {
    $('html, body').animate({
      scrollTop: $('.feedback-list').offset().top
    }, 500);
    alreadyScrolled = true; // Меняем флаг после прокрутки
  }
});


//$(document).ready(function() {
//    // Проверяем состояние кнопок при загрузке страницы
//    checkButtonFavourite();
//
//    $("#add-favourite").click(function() {
//      $(this).parent().hide();
//      $("#delete-favourite").parent().show();
//      // Сохраняем состояние в LocalStorage
//      localStorage.setItem("favourite", "deleted");
//    });
//
//    $("#delete-favourite").click(function() {
//      $(this).parent().hide();
//      $("#add-favourite").parent().show();
//      // Сохраняем состояние в LocalStorage
//      localStorage.setItem("favourite", "added");
//    });
//
//    // Функция проверки состояния
//    function checkButtonFavourite() {
//      let checkFavourite = localStorage.getItem("favourite");
//      if (checkFavourite === "deleted") {
//        $("#add-favourite").parent().hide();
//        $("#delete-favourite").parent().show();
//      } else {
//        $("#delete-favourite").parent().hide();
//        $("#add-favourite").parent().show();
//      }
//    }
//});

//Карусель main_page.html
let mainAssortment = $('.main-assortment'),
    mainCouruselAssortment = $('.main-courusel-assortment'),
    countMainAssortment = mainAssortment.length,
    mainPosition = 0,
    mainStep = 200;
    mainMax = (countMainAssortment * 200) - 800;

$(mainCouruselAssortment).width(200 * countAssortment);
$('.main-next').click(function () {
    if (mainPosition == -mainMax) {
        mainPosition = 0;
        mainCouruselAssortment.css("left", mainPosition + "px");
    }else{
        mainPosition = mainPosition - mainStep;
        mainCouruselAssortment.css("left", mainPosition + "px");
    }
});

$('.main-prev').click(function () {
    if (mainPosition == 0) {
        mainPosition = -mainMax;
        mainCouruselAssortment.css("left", mainPosition + "px");
    }else{
        mainPosition = mainPosition + mainstep;
        mainCouruselAssortment.css("left", mainPosition + "px");
    }
});