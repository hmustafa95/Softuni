function editElement(sentence, original, replacer) {
    let text = sentence.textContent;

    while (text.includes(original)) {
        text = text.replace(original, replacer);
    }
    sentence.textContent = text;
}
