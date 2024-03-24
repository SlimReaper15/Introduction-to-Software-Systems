// Toggle the navigation menu visibility on mobile devices
const navSlide = () => {
    const mobile_menu = document.querySelector('.mobile-menu');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');

    mobile_menu.addEventListener('click', () => {
        nav.classList.toggle('nav-active');

        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = '';
            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.3}s`;
            }
        });
    });
}

navSlide();

// Slide in words in the slider on page load
document.addEventListener("DOMContentLoaded", function () {
    const words = document.querySelectorAll(".slider-text");

    function slideInWords() {
        words.forEach((word, index) => {
            setTimeout(() => {
                word.style.opacity = "1";
                word.style.transform = "translateX(0)";
            }, index * 1000);
        });
    }

    slideInWords();
});

// Handle book slides functionality
document.addEventListener("DOMContentLoaded", function () {
    const bookSlides = document.querySelector(".book-slides");
    let currentSlide = 0;

    function showSlide(index) {
        currentSlide = index;
        updateSlideVisibility();
    }

    function updateSlideVisibility() {
        const slides = bookSlides.children;
        for (let i = 0; i < slides.length; i++) {
            slides[i].style.display = i === currentSlide ? "block" : "none";
        }
    }

    window.changeSlide = function (direction) {
        currentSlide = (currentSlide + direction + bookSlides.children.length) % bookSlides.children.length;
        updateSlideVisibility();
    };

    updateSlideVisibility();
});

// Toggle the 'active' class on flashcards when clicked
document.addEventListener('DOMContentLoaded', function () {
    const flashcards = document.querySelectorAll('.flashcard');

    flashcards.forEach(flashcard => {
        flashcard.addEventListener('click', function () {
            this.classList.toggle('active');
        });
    });
});

// Toggle dark mode for the entire page
const darkModeToggle = document.getElementById('darkModeToggle');
const body = document.body;
const nav = document.querySelector('nav');
const navLinks = document.querySelectorAll('.nav-links a');

darkModeToggle.addEventListener('change', toggleMode);

function toggleMode() {
  body.classList.toggle('dark-mode');
  nav.classList.toggle('dark-mode');

  const navLinksInNav = nav.querySelectorAll('.nav-links a');
  navLinksInNav.forEach(link => link.classList.toggle('dark-mode'));
}
