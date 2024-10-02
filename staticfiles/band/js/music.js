document.addEventListener('DOMContentLoaded', function() {
    const audioPlayer = document.getElementById('audioPlayer');
    const audioSource = document.getElementById('audioSource');
    const trackList = document.querySelectorAll('.music-list ul li');

    trackList.forEach(track => {
        track.addEventListener('click', function() {
            const src = this.getAttribute('data-src');
            audioSource.src = src;
            audioPlayer.load();
            audioPlayer.play();
        });
    });
});