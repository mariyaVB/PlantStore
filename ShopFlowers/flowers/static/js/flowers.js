//document.addEventListener('DOMContentLoaded', function() {
//    const form = document.querySelector('form[name=filter]');
//    const flowersList = document.getElementById('flowers-list-id');
//
//    form.addEventListener('submit', (event) => {
//    event.preventDefault();
//    const formData = new FormData(form);
//    const urlParams = new URLSearchParams(formData);
//    const url = form.action + '?' + urlParams.toString();
//
//    fetch(url)
//        .then(response => response.json())
//        .then(data => {
//            renderProducts(data);
//        })
//        .catch(error => {
//            console.error('Ошибка при отправке запроса:', error);
//        });
//    });
//
//        function renderProducts(products) {
//            flowersList.innerHTML = '';
//            products.forEach(product => {
//                flowersList.innerHTML = `
//                    <div class="flower">
//                         <a href="/flower/${product.slug}/">
//                             <img src="${product.image}" alt="${product.name}">
//                         </a>
//                         <div class="flower-detail">
//                             <p class="p-text">${product.name}</p>
//                             <p class="p-text">от ${product.price}₽</p>
//                             ${product.quantity > 0 ?
//                                 `<a href="/add-cart/${product.id}/" class="cart-button">Добавить в корзину</a>` :
//                                 '<p style="margin: 5px;">Нет в наличии</p>'
//                             }
//                         </div>
//                    </div>
//                `;
//            });
//        }

// document.addEventListener('DOMContentLoaded', function() {
//     const form = document.querySelector('input[name=category]');
//     const flowersListContainer = document.getElementById('flowers-list-id');

//     form.addEventListener('submit', (event) => {
//         event.preventDefault();
//         const formData = new FormData(form);
//         const urlParams = new URLSearchParams(formData);
//         const url = form.action + '?' + urlParams.toString();

//         fetch(url)
//             .then(response => response.json())
//             .then(data => {
//                 renderProducts(data);
//             })
//             .catch(error => {
//                 console.error('Ошибка при отправке запроса:', error);
//             });
//     });

//     function renderProducts(products) {
//         flowersListContainer.innerHTML = ''; // Очищаем контейнер

//         products.forEach(product => {
//             const productDiv = document.createElement('div');
//             productDiv.innerHTML = `
//                 <div class="flower">
//                 <a href="/flower/${product.slug}/">
//                     <img src="${product.image}" alt="${product.name}">
//                 </a>
//                 <div class="flower-detail">
//                     <p class="p-text">${product.name}</p>
//                     <p class="p-text">от ${product.price}₽</p>
//                     ${product.quantity > 0 ?
//                         `<a href="/add-cart/${product.id}/" class="cart-button">Добавить в корзину</a>` :
//                         '<p style="margin: 5px;">Нет в наличии</p>'
//                     }
//                 </div>
//                 </div>
//             `;
//             flowersListContainer.appendChild(productDiv);
//         });
//     }
// });


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