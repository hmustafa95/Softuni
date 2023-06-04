function sumTable() {
    let result = document.getElementById('sum');
    let numbers = Array.from(document.querySelectorAll('tr td:nth-child(2)'));
    let sum = 0;
    
    for (let num of numbers) {
        sum += Number(num.textContent);
    }

    result.textContent = sum;
}