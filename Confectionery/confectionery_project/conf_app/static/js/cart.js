// function showToast(message) {
//     const toastContainer = document.getElementById('toast-container');
//     const toast = document.createElement('div');
//     toast.className = 'toast';
//     toast.textContent = message;
//     toastContainer.appendChild(toast);

//     setTimeout(() => toast.classList.add('show'), 100);
//     setTimeout(() => {
//         toast.classList.remove('show');
//         setTimeout(() => toast.remove(), 300);
//     }, 3000);
// }

// document.addEventListener('DOMContentLoaded', () => {
//     document.querySelectorAll('.add-to-cart').forEach(button => {
//         button.addEventListener('click', (event) => {
//             event.preventDefault();
//             const productId = button.getAttribute('data-product-id');

//             fetch(`/add-to-cart/${productId}/`, {
//                 method: 'GET',
//                 headers: {
//                     'X-Requested-With': 'XMLHttpRequest',
//                 },
//             })
//             .then(response => response.json())
//             .then(data => {
//                 showToast(`Товар "${data.product_title}" добавлен в корзину!`);
//                 document.querySelector('#total-sum').textContent = `${data.total_sum} тг`;
//             })
//             .catch(error => console.error('Ошибка при добавлении товара в корзину:', error));
//         });
//     });
// });

function showToast(message) {
    const toastContainer = document.getElementById('toast-container');
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.textContent = message;
    toastContainer.appendChild(toast);

    setTimeout(() => toast.classList.add('show'), 100);
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

document.addEventListener('DOMContentLoaded', () => {
    // Обработчик для кнопок уменьшения количества
    document.querySelectorAll('.decrease-btn').forEach(button => {
        button.addEventListener('click', (event) => {
            event.preventDefault();
            const productId = button.closest('.cart-item').getAttribute('data-product-id');

            fetch(`/decrease-quantity/${productId}/`, {
                method: 'GET',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.quantity === 0) {
                    button.closest('.cart-item').remove(); // Удаляем элемент из корзины, если количество 0
                } else {
                    button.closest('.quantity').querySelector('.quantity-value').textContent = data.quantity;
                }
                document.querySelector('#total-sum').textContent = `${data.total_sum} тг`;
                showToast(`Количество товара уменьшено.`);
            })
            .catch(error => console.error('Ошибка при уменьшении количества товара:', error));
        });
    });

    // Обработчик для кнопок увеличения количества
    document.querySelectorAll('.increase-btn').forEach(button => {
        button.addEventListener('click', (event) => {
            event.preventDefault();
            const productId = button.closest('.cart-item').getAttribute('data-product-id');

            fetch(`/increase-quantity/${productId}/`, {
                method: 'GET',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                },
            })
            .then(response => response.json())
            .then(data => {
                button.closest('.quantity').querySelector('.quantity-value').textContent = data.quantity;
                document.querySelector('#total-sum').textContent = `${data.total_sum} тг`;
                showToast(`Количество товара увеличено.`);
            })
            .catch(error => console.error('Ошибка при увеличении количества товара:', error));
        });
    });

    // Обработчик для добавления товара в корзину
    document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', (event) => {
            event.preventDefault();
            const productId = button.getAttribute('data-product-id');

            fetch(`/add-to-cart/${productId}/`, {
                method: 'GET',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                },
            })
            .then(response => response.json())
            .then(data => {
                showToast(`Товар "${data.product_title}" добавлен в корзину!`);
                document.querySelector('#total-sum').textContent = `${data.total_sum} тг`;
            })
            .catch(error => console.error('Ошибка при добавлении товара в корзину:', error));
        });
    });
});

