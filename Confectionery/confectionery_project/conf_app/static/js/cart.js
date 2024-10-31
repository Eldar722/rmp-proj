document.addEventListener('DOMContentLoaded', () => {
    // Находим все элементы с классом add-to-cart
    document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', (event) => {
            event.preventDefault(); // Отменяем стандартное поведение ссылки

            // Получаем ID товара из атрибута data-product-id
            const productId = button.getAttribute('data-product-id');
            if (!productId) {
                console.error('ID продукта не найден.');
                return;
            }

            // Отправляем запрос на добавление товара в корзину
            fetch(`/add-to-cart/${productId}/`, {
                method: 'GET',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                },
            })
            .then(response => response.json())
            .then(data => {
                // Выводим уведомление или обновляем количество товаров в корзине
                console.log(`Товар ${data.product_name} добавлен в корзину. Текущее количество: ${data.quantity}`);
                document.querySelector('#total-sum').textContent = `${data.total_sum} тг`;

                // Обновляем интерфейс, если требуется, например, значок корзины
                const cartIconCount = document.querySelector('#cart-icon-count');
                if (cartIconCount) {
                    cartIconCount.textContent = parseInt(cartIconCount.textContent) + 1;
                }
            })
            .catch(error => console.error('Ошибка при добавлении товара в корзину:', error));
        });
    });
});
