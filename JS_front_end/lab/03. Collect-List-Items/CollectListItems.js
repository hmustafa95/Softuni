function extractText() {
    let items = Array.from(document.querySelectorAll('ul#items li'));
    let result = document.querySelector('#result');
    for (let note of items) {
        result.value += note.textContent + '\n';
    }
}