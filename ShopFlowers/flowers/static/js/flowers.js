function ajaxSend(url, params) {
    fetch(`${url}?${params}`, {
    method: 'GET',
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
    .then(response => response.json())
    .then(json => render(json))
    .catch(error => console.error(error))
}

const forms = document.querySelector('form[name=filter]');

forms.addEventListener('submit', function (e) {
    e.preventDefault();
    let url = this.action;
    let params = new URLSearchParams(new FormData(this)).toString();
    ajaxSend(url, params);
});

function render(data) {
    let template = Hogan.compile(html);
    let output = template.render(data);
    const div = document.querySelector('.flowers-list');
    div.innerHTML = output;
}

let html = '\

{{#flowers}}\
    <a href="{% url 'flower' slug=flower.slug %}">\
    <div class="flower">\
        <img src="{{ flower.image.url }}">\
        <div class="flower-detail">\
            <p class="p-text">{{ flower.title }}</p>\
            <p class="p-text">от {{ flower.price }}₽</p>\
            {% if flower.quantity > 0 %}\
                <button class="cart-button" type="submit">Добавить в корзину</button>\
            {% else %}\
                <p>Нет в наличии</p>\
            {% endif %}\
        </div>\
    </div>\
    </a>\
{{/flowers}}'

