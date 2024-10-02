/* static/band/js/parallax.js */

document.addEventListener('mousemove', function(e) {
    const x = e.clientX / window.innerWidth * 50;
    const y = e.clientY / window.innerHeight * 50;
    const parallax = document.querySelector('body');
    parallax.style.backgroundPosition = `${x * 0.5}% ${y * 1}%`;
});
