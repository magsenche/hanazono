if (typeof HTTP_HOST === 'undefined') {
    console.error("HTTP_HOST is not defined. Ensure server_config.js is loaded before this script.");
}
document.addEventListener('DOMContentLoaded', function () {
    function updateMarkdownContent(id, isOk) {
        fetch('http://' + HTTP_HOST + '/update_markdown', {
            method: 'POST',
            body: new URLSearchParams({ id: id, is_ok: isOk }),
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
        })
            .then(response => {
                if (response.ok) {
                    console.log('Markdown content updated successfully.')
                } else {
                    console.error('Failed to update Markdown content.')
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
    function generateQuizContent() {
        fetch('http://' + HTTP_HOST + '/generate_quiz', {
            method: 'POST',
            body: new URLSearchParams({}),
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
        })
            .then(response => {
                if (response.ok) {
                    console.log('Quiz content generated updated successfully.')
                } else {
                    console.error('Failed to generate quiz content.')
                }
            })
            .catch(error => {
                console.error('Error:', error)
            });
    }
    const qbutton = document.querySelector('.qbutton')
    if (qbutton) {
        qbutton.addEventListener('click', function (event) {
            event.preventDefault();
            generateQuizContent()
        })
    }
});
