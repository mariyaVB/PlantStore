// Убавляем кол-во по клику
    $('.quantity_inner .bt_minus').click(function() {
    let $input = $(this).parent().find('.quantity');
    let count = parseInt($input.val()) - 1;
    count = count < 1 ? 1 : count;
    $input.val(count);
});
// Прибавляем кол-во по клику
$('.quantity_inner .bt_plus').click(function() {
    let $input = $(this).parent().find('.quantity');
    let count = parseInt($input.val()) + 1;
    count = count > parseInt($input.data('max-count')) ? parseInt($input.data('max-count')) : count;
    $input.val(parseInt(count));
});
// Убираем все лишнее и невозможное при изменении поля
$('.quantity_inner .quantity').bind("change keyup input click", function() {
    if (this.value.match(/[^0-9]/g)) {
        this.value = this.value.replace(/[^0-9]/g, '');
    }
    if (this.value == "") {
        this.value = 1;
    }
    if (this.value > parseInt($(this).data('max-count'))) {
        this.value = parseInt($(this).data('max-count'));
    }
});


document.addEventListener('DOMContentLoaded', function() {
    const delivery = document.getElementById('inputDelivery');
    const address = document.getElementById('address'); 
    const takingSumm = document.getElementById('takingSumm'); 
    const totalSumm = document.getElementById('totalSumm'); 
    const initialTotalSumm = parseInt(totalSumm.textContent.replace(' ₽', ''));
    const DELIVERY_COST = 500;
    const SELF_COST = 0;



    function toggleAddress() {
        if (delivery.value === 'Доставка') {
            address.style.display = 'block';
            takingSumm.textContent = 'Стоимость доставки: ' + DELIVERY_COST + '₽';

            } else {
                address.style.display = 'none';
                takingSumm.textContent = 'Стоимость доставки: ' + SELF_COST + '₽';
            }
        }

        function updateTotalSum() {
            let newTotalSumm = initialTotalSumm;
            let takingSummValue = 0;
            if (delivery.value === 'Доставка') {
                newTotalSumm += DELIVERY_COST;
                takingSummValue = DELIVERY_COST;
            }
            totalSumm.textContent = 'Итого: ' + newTotalSumm + ' ₽';
            document.getElementById('hiddenTakingSumm').value = takingSummValue;
            document.getElementById('hiddenTotalSumm').value = newTotalSumm;
        }

        toggleAddress();
        updateTotalSum(); // Вызываем при загрузке страницы
        delivery.addEventListener('change', function() {
            toggleAddress();
            updateTotalSum(); // Вызываем при изменении типа доставки
        });
});



