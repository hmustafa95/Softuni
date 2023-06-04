function deleteByEmail() {
    let items = document.querySelectorAll('tr td:nth-child(2)');
    let email = document.getElementsByName('email')[0].value;
    for (let td of items) {
        if (td.textContent == email) {
            let row = td.parentNode;
            row.parentNode.removeChild(row);
            document.getElementById('result').textContent = 'Deleted.';
            return;
        }
    document.getElementById('result').textContent = 'Not found.';
    }
}