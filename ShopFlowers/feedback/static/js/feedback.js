$(document).ready(function() {
    let ratingValue = $('#hiddenRating').val();
    console.log(ratingValue);
    console.log(typeof +ratingValue);
    let star = $('.star');
    for (let i = 0; i < +ratingValue; i++) {
        console.log(star.val());
        star[i].style.color = 'rgba(255, 237, 75, 1)'; 
    };

    $('.star').click(function() {
        event.preventDefault();
        $(this).prevAll().andSelf().css('color', 'rgba(255, 237, 75, 1)');
        $(this).nextAll().css('color', 'rgba(15, 15, 15, 1)'); 

        let newRatingValue = $(this).val();  // Получаем значение value кнопки
        // console.log(typeof newRatingValue);
      $('#hiddenRating').val(newRatingValue); // Устанавливаем значение в скрытое поле
      
      console.log($('#hiddenRating').val()); 
    });
}); 

// for (let i = 0; i < one.length; i++) {   
//     one[i].style.background = 'Pink';
//     one[i].style.border = '5px double black';
// }