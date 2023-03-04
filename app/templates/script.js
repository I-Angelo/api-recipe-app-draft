document.addEventListener('DOMContentLoaded' , () => {
    const toggleButton = document.getElementsByClassName('toggle-button')[0]
    const navbarLinks = document.getElementsByClassName('navbar-links')[0]

    toggleButton.addEventListener('click', () => {
    navbarLinks.classList.toggle('active')
});

});

// creating the code or rather wrapping it up under the code in line 1 is for this code to load before html is fully loaded
