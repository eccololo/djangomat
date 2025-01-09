// Scrolling up alert message that it will dissapear after 5 seconds
setTimeout(function() {
    $("#messages").slideUp("slow");
}, 5000);

// Code for search bar on home page to search for automation tasks.
document.addEventListener('DOMContentLoaded', function () {
    const searchBar = document.getElementById('searchBar');
    const taskContainer = document.getElementById('taskContainer');
    const cards = taskContainer.getElementsByClassName('col-md-4');

    searchBar.addEventListener('input', function () {
        const filter = searchBar.value.toLowerCase();

        Array.from(cards).forEach(card => {
            const title = card.querySelector('.card-title').innerText.toLowerCase();
            if (title.includes(filter)) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
            
            // Deleting top margin after search to align card good
            card.classList.remove('mt-5');
        });

        if (filter === '') {
            Array.from(cards).forEach((card, index) => {
                if (index >= 3) {
                    // Adding top margin to tasks cards but not to first 3 when search field is empty.
                    card.classList.add('mt-5');
                }
            });
        }
    });
});