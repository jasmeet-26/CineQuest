document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('recommendation-form');
    form.addEventListener('submit', function (event) {
        event.preventDefault();
        const movie = document.getElementById('movie').value;

        fetch('/recommend', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ movie: movie }),
        })
        .then(response => response.json())
        .then(data => {
            const recommendationsContainer = document.getElementById('recommendations-container');
            const recommendationsDiv = document.getElementById('recommendations');

            if (data.error) {
                recommendationsDiv.innerHTML = `<h2>Error:</h2><p>${data.error}</p>`;
            } else {
                recommendationsDiv.innerHTML = '<h2>Recommendations:</h2>';
                data.forEach(m => {
                    const recommendationBox = document.createElement('div');
                    recommendationBox.classList.add('recommendation-box');
                    recommendationBox.innerHTML = `<p>${m}</p>`;
                    recommendationsDiv.appendChild(recommendationBox);
                });
            }
            recommendationsContainer.style.display = 'block';
        })
        .catch(error => {
            console.error('Error:', error);
            const recommendationsContainer = document.getElementById('recommendations-container');
            const recommendationsDiv = document.getElementById('recommendations');
            recommendationsDiv.innerHTML = `<h2>Error:</h2><p>There was an error processing your request.</p>`;
            recommendationsContainer.style.display = 'block';
        });
    });
});
