//function ajaxSend(url, params) {
//    // Отправляем запрос
//    fetch(`${url}?${params}`, {
//        method: 'GET',
//        headers: {
//            'Content-Type': 'application/x-www-form-urlencoded',
//        },
//    })
//        .then(response => response.json())
//        .then(json => render(json))
//        .catch(error => console.error(error))
//}
//
//const forms = document.querySelector('form[name=filter]');
//
//forms.addEventListener('submit', function (e) {
//
//    e.preventDefault();
//    let url = this.action;
//    let params = new URLSearchParams(new FormData(this)).toString();
//    ajaxSend(url, params);
//});
//
//function render(json) {
//    const flowersList = document.getElementById('flowers-list-id');
//
//    flowersList.innerHTML = '';
//
//    // Цикл по найденным цветам
//    for (const flower of json.flowers) {
//        const flowerHTML = `
//            <div class="flower">
//                <a href="/flowers/${flower.slug}/">
//                    <img src="/media/${flower.image}" width="250px" height="300px">
//                </a>
//                ${flower.is_discount ? `<div class="product-discount"><span>${flower.discount.percent}%</span></div>` : ''}
//                <div class="flower-detail">
//                    <p class="p-text">${flower.title}</p>
//                    ${flower.is_discount ? `<div class="flower-price"><p class="p-price-discount">от ${flower.calculate_the_price}₽</p><p class="p-price">${flower.price}₽</p></div>` : `<p class="p-text">от ${flower.calculate_the_price}₽</p>`}
//                    ${flower.quantity > 0 ? `<a href="/cart/add-cart/${flower.id}/" class="cart-button">Добавить в корзину</a>` : `<p style="margin: 5px; color: rgba(40, 49, 6, 1);">Нет в наличии</p>`}
//                </div>
//            </div>
//        `;
//
//        flowersList.innerHTML += flowerHTML; // Добавляем HTML-код в контейнер
//    }
//}


//Карусель
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
