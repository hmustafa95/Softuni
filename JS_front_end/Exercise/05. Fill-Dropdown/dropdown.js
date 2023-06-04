function addItem() {
    let text = document.getElementById('newItemText');
    let textValue = document.getElementById('newItemValue');

    let newOption = document.createElement('option');
    newOption.textContent = text.value;
    newOption.value = textValue.value;

    document.getElementById('menu').appendChild(newOption);
    text.value = '';
    textValue.value = '';
}