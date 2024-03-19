if (typeof HTTP_HOST === 'undefined') {
    console.error("HTTP_HOST is not defined. Ensure server_config.js is loaded before this script.");
}
document.addEventListener('DOMContentLoaded', function () {
    function updateMarkdownContent(id, isOk) {
        fetch('http://' + HTTP_HOST + '/update_flashcard/' + id + '/' + isOk, {
            method: 'GET',
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    console.log('Flashcard updated successfully.');
                    displayFlashcardsPopup(isOk, data);
                } else {
                    console.error('Failed to update Flashcard.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
    const fbuttons = document.querySelectorAll('.fbutton.ok, .fbutton.nok');
    fbuttons.forEach(function (fbutton) {
        fbutton.addEventListener('click', function (event) {
            event.preventDefault();

            const details = fbutton.closest('.question');
            const sectionButtons = details.querySelectorAll('.fbutton.ok, .fbutton.nok');
            sectionButtons.forEach(function (sectionButton) {
                sectionButton.classList.add('disabled');
            });

            const idElement = details.querySelector('h5');
            const id = idElement ? idElement.id.split('-')[2] : null;

            if (id !== null) {
                if (fbutton.classList.contains('ok')) {
                    updateMarkdownContent(id, true);
                } else if (fbutton.classList.contains('nok')) {
                    updateMarkdownContent(id, false);
                }
            }
        });
    });
    function displayFlashcardsPopup(isOk, data) {
        let popup = document.createElement('div');
        popup.classList.add('flashcard-popup');
        popup.classList.add('md-typeset');
        popup.innerHTML = `Box: <strong>${data.box}</strong><br>Score: <strong>${data.score}</strong><br>Next Review: <strong>${data.next_review_date}</strong>`;
        if (isOk) {
            popup.classList.add('flashcard-green');
        } else {
            popup.classList.add('flashcard-red');
        }
        let sidebarInner = document.querySelector('.md-main');
        sidebarInner.insertAdjacentElement('afterend', popup)
        setTimeout(() => {
            if (popup.parentElement) {
                popup.parentElement.removeChild(popup);
            }
        }, 2000);
    }
});
