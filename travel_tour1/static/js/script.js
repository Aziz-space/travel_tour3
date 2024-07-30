document.addEventListener('DOMContentLoaded', function() {
    const burgerMenu = document.querySelector('.burger-menu');
    const navLinks = document.querySelector('.nav-links');
    const navCategories = document.querySelector('.nav-categories');
    const homeTitle = document.querySelector('.home_title'); // Выбираем элемент home_title

    burgerMenu.addEventListener('click', function() {
        navLinks.classList.toggle('active');
        navCategories.classList.toggle('active');

        // Добавляем или удаляем класс 'burger-menu-open' у элемента home_title
        homeTitle.classList.toggle('burger-menu-open');
    });
});



