function addItem() {
    let text = document.getElementById('newItemText').value;
    let parentElement = document.getElementById('items');
    let newLi = document.createElement('li');
    newLi.appendChild(document.createTextNode(text));
    parentElement.appendChild(newLi);
    document.getElementById('newItemText').value = '';
}