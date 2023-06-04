function colorize() {
    let selection = Array.from(document.querySelectorAll('tr:nth-of-type(2n)'));
    selection.forEach(td => td.style.backgroundColor = 'teal');
}