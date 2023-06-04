function extractText() {
    let itemNodes = document.querySelectorAll("ul#items li");
    let textarea = document.querySelector("#result");
    for (let note of itemNodes) {
        textarea.value += node.textContent + "\n";
    }
}