//profile.html
////Меню личного кабинета
//$('.bt-my-orders').click(function () {
////    $('.bt-my-orders').css('backgroundColor', 'rgba(114, 121, 88, 1)');
//    $('.popup-my-settings').hide();
//    $('.popup-my-feedback').hide();
//    $('.popup-my-like').hide();
//    $('.popup-my-cart').hide();
//    $('.popup-my-orders').show();
//});
//
//$('.bt-my-profile').click(function () {
////    $('.bt-my-profile').css('backgroundColor', 'rgba(114, 121, 88, 1)');
//    $('.popup-my-settings').show();
//    $('.popup-my-orders').hide();
//    $('.popup-my-feedback').hide();
//    $('.popup-my-like').hide();
//    $('.popup-my-cart').hide();
//});
//
//$('.bt-my-feedback').click(function () {
//    $('.popup-my-settings').hide();
//    $('.popup-my-orders').hide();
//    $('.popup-my-like').hide();
//    $('.popup-my-cart').hide();
//    $('.popup-my-feedback').show();
//});
//
//$('.bt-my-like').click(function () {
//    $('.popup-my-settings').hide();
//    $('.popup-my-orders').hide();
//    $('.popup-my-like').show();
//    $('.popup-my-cart').hide();
//    $('.popup-my-feedback').hide();
//});
//
//$('.bt-my-cart').click(function () {
//    $('.popup-my-settings').hide();
//    $('.popup-my-orders').hide();
//    $('.popup-my-like').hide();
//    $('.popup-my-cart').show();
//    $('.popup-my-feedback').hide();
//});

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

