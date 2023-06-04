function solve(num) {
    let result = 0;
    let digits = num.toString().split('');
    let check = false;
    for (let i = 0; i < digits.length; i++) {
        result += parseInt(digits[i]);
        if (digits[i] === digits[0]) {
            check = true;
        }
        else {
            check = false;
        }
    }
    console.log(check);
    console.log(result);
}

solve(2222222)