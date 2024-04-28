document.getElementById('genreForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var genre = document.getElementById('genre').value;
    
    fetch('/recommend', {
        method: 'POST',
        body: new URLSearchParams({
            'genre': genre
        }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
    .then(response => response.text())
    .then(data => {
        
        document.getElementById('recommendation').innerText = data;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

jQuery(document).ready(function() {
    $('[data-youtube]').youtube_background();
});
