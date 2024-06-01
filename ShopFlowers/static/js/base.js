$('.bt-my-orders').click(function () {
//    $('.bt-my-orders').css('backgroundColor', 'rgba(114, 121, 88, 1)');
    $('.popup-my-settings').hide();
    $('.popup-my-feedback').hide();
    $('.popup-my-like').hide();
    $('.popup-my-cart').hide();
    $('.popup-my-orders').show();
});

$('.bt-my-profile').click(function () {
//    $('.bt-my-profile').css('backgroundColor', 'rgba(114, 121, 88, 1)');
    $('.popup-my-settings').show();
    $('.popup-my-orders').hide();
    $('.popup-my-feedback').hide();
    $('.popup-my-like').hide();
    $('.popup-my-cart').hide();
});

$('.bt-my-feedback').click(function () {
    $('.popup-my-settings').hide();
    $('.popup-my-orders').hide();
    $('.popup-my-like').hide();
    $('.popup-my-cart').hide();
    $('.popup-my-feedback').show();
});

$('.bt-my-like').click(function () {
    $('.popup-my-settings').hide();
    $('.popup-my-orders').hide();
    $('.popup-my-like').show();
    $('.popup-my-cart').hide();
    $('.popup-my-feedback').hide();
});

$('.bt-my-cart').click(function () {
    $('.popup-my-settings').hide();
    $('.popup-my-orders').hide();
    $('.popup-my-like').hide();
    $('.popup-my-cart').show();
    $('.popup-my-feedback').hide();
});

function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}


//window.onclick = function(event) {
//  if (!event.target.matches('.drop-btn')) {
//    var dropdowns = document.getElementsByClassName("dropdown-content");
//    var i;
//    for (i = 0; i < dropdowns.length; i++) {
//      var openDropdown = dropdowns[i];
//      if (openDropdown.classList.contains('show')) {
//        openDropdown.classList.remove('show');
//      }
//    }
//  }
//}