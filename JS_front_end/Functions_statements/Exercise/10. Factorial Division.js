function factorial(num1, num2) {
    let fact1 = 1;
    let fact2 = 1;
    for (let i = 1; i <= num1; i++) {
        fact1 *= i;
    }
    for (let y = 1; y <= num2; y++) {
        fact2 *= y;
    }
    result = fact1 / fact2;
    console.log(result.toFixed(2));
}