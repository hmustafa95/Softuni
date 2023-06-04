function addItem() {
    let newItem = document.getElementById('newItemText').value;
    let list = document.getElementById('items');

    if (list.length === 0) return;

    let listItem = document.createElement('li');
    listItem.textContent = newItem;

    let remove = document.createElement('a');
    let linkText = document.createTextNode('[Delete]');
    remove.appendChild(linkText);
    remove.href = '#';
    remove.addEventListener('click', deleteItem);

    listItem.appendChild(remove);
    list.appendChild(listItem);

    function deleteItem() {
        listItem.remove();
    }
}