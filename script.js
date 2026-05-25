// JavaScript для Booking.com

// Функция поиска отелей
function searchHotels() {
    const destination = document.getElementById('destination').value;
    const checkin = document.getElementById('checkin').value;
    const checkout = document.getElementById('checkout').value;
    const guests = document.getElementById('guests').value;
    
    console.log('Поиск отелей:');
    console.log('Направление:', destination);
    console.log('Заезд:', checkin);
    console.log('Выезд:', checkout);
    console.log('Гостей:', guests);
    
    // Здесь будет AJAX запрос к API
    alert(`Поиск отелей в городе: ${destination}`);
}

// Фильтрация отелей по цене
function filterByPrice(maxPrice) {
    const hotels = document.querySelectorAll('.hotel-card');
    hotels.forEach(hotel => {
        const price = parseInt(hotel.querySelector('.price').innerText);
        if (price > maxPrice) {
            hotel.style.display = 'none';
        }
    });
}

// Добавление в избранное
function addToFavorites(hotelId) {
    localStorage.setItem('favorite_' + hotelId, 'true');
    alert('Добавлено в избранное!');
}

// Инициализация при загрузке страницы
document.addEventListener('DOMContentLoaded', function() {
    console.log('Booking.com app loaded');
});