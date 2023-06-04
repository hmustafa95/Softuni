function solve(num) {
    let result = 0;
    let digits = num.toString().split('');
    for (let i = 0; i < digits.length; i++) {
        result += parseInt(digits[i]);
    }
    console.log(result);
}

solve(15)