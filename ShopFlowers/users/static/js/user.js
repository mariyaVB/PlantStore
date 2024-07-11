//profile.html

//Изменить фото
$('.bt-user-change').mouseover(function () {
    $('.photo-change').show();
});

$('.bt-user-change').mouseout(function () {
    $('.photo-change').hide();
});



// Модальное окно reset_password_done.html
$('.bt-reset').click(function () {
    $('.overlay').show;
});


// Заказы в профиле
$('.more').click(function () {
    $('.order-img-7-12-slice-two').show();
    $('.order-img-7-12-slice-one').hide();
    $('.more').hide();
    $('.many').show();
});

$('.many').click(function () {
    $('.order-img-7-12-slice-two').toggle();
    $('.order-img-7-12-slice-one').toggle();
    $('.more').toggle();
    $('.many').toggle();
});



// Вкладки в заказах
$(document).ready(function() {
    let flag = $('.flag-status').val();
    console.log(flag)
    // Начальная стилизация
    if (flag == 'Создан' | flag == 'В обработке' | flag == 'Готов') {
        $('#status-progress').addClass('active');
        $('#status-completed, #status-cancel').addClass('not-active');
    } 
    else if (flag == 'Выполнен') {
        $('#status-completed').addClass('active');
        $('#status-progress, #status-cancel').addClass('not-active');
    }
    else if (flag == 'Отменен') {
        $('#status-cancel').addClass('active');
        $('#status-progress, #status-completed').addClass('not-active');
    } else {
        console.log(flag)
    }

    // $('#status-all').addClass('active');
    // $('#status-progress, #status-completed, #status-cancel, #status-feedback').addClass('not-active');

    // Обработчики кликов
    $('#status-all, #status-progress, #status-completed, #status-cancel, #status-feedback').click(function() {
        // Отправить форму        
        document.forms['order-filter'].submit();

        // Переключать классы
        // $(this).toggleClass('active not-active');
        // $('#status-all, #status-progress, #status-completed, #status-cancel, #status-feedback').not(this).addClass('not-active');
       
    });
});


// Оценить товары в заказе
$('.bt-rating').click(function() {
  $('.feedback-order').toggle();
  $('.popup').css({
    'position': 'sticky',
    'top': '0',
    'background': 'rgba(234, 233, 229, 1)'
    });
});

$('.bt-close').click(function() {
    $('.feedback-order').toggle();
    $('.popup').css({
        'position': 'static',
        'background': 'none'
    });
});



// Рейтинг в отзывах

$(document).ready(function() {
    $('.star').click(function() {
        event.preventDefault();
        $(this).prevAll().andSelf().css('color', 'rgba(255, 237, 75, 1)');
        $(this).nextAll().css('color', 'rgba(15, 15, 15, 1)'); 

        let ratingValue = $(this).val();  // Получаем значение value кнопки
        // console.log(typeof ratingValue);
        // ratingValue = +ratingValue;
      $('#hiddenRating').val(ratingValue); // Устанавливаем значение в скрытое поле
      
      console.log($('#hiddenRating').val()); 
    });
}); 



