if (typeof HTTP_HOST === 'undefined') {
    console.error("HTTP_HOST is not defined. Ensure server_config.js is loaded before this script.");
}
document.addEventListener('DOMContentLoaded', function () {
    function displayFlashcardsPopup() {
        fetch('http://' + HTTP_HOST + '/notes/quiz/', {
            method: 'GET',
        })
            .then(response => response.text())
            .then(content => {
                // Create a popup div to display the content
                let popup = document.createElement('div');
                popup.classList.add('flashcard-popup'); // Add class for easier targeting
                popup.innerHTML = content;
                document.body.appendChild(popup);

                // Add event listener to close popup when clicking outside
                document.body.addEventListener('click', function (event) {
                    // Check if clicked target is not the popup or a descendant of the popup
                    if (!popup.contains(event.target) && event.target !== popup) {
                        document.body.removeChild(popup);
                        // Remove the event listener once popup is closed
                        document.body.removeEventListener('click', arguments.callee);
                    }
                }, false);

                // Prevent event from propagating to the body when clicking inside the popup
                popup.addEventListener('click', function (event) {
                    event.stopPropagation();
                });

            })
            .catch(error => {
                console.error('Error:', error);
            });
    }

    const popbutton = document.querySelector('.popbutton');
    if (popbutton) {
        popbutton.addEventListener('click', function (event) {
            event.preventDefault();
            event.stopPropagation(); // Prevent click event from propagating to body immediately after opening the popup
            displayFlashcardsPopup();
        });
    }


    function updateMarkdownContent(id, isOk) {
        fetch('http://' + HTTP_HOST + '/update_flashcard/' + id + '/' + isOk, {
            method: 'GET',
        })
            .then(response => {
                if (response.ok) {
                    console.log('Flashcard updated successfully.')
                } else {
                    console.error('Failed to update Flashcard.')
                }
            })
            .catch(error => {
                console.error('Error:', error)
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
            const id = idElement ? idElement.id.split('-')[1] : null;

            if (id !== null) {
                if (fbutton.classList.contains('ok')) {
                    updateMarkdownContent(id, true);
                } else if (fbutton.classList.contains('nok')) {
                    updateMarkdownContent(id, false);
                }
            }
        });
    });
});
