function sign(num1, num2, num3) {
    if ((num1 < 0 && num2 < 0 && num3 < 0) || (num1 < 0 && num2 >= 0 && num3 >= 0) || (num1 >= 0 && num2 < 0 && num3 >= 0) || (num1>= 0 && num2 >= 0 && num3 < 0)) {
        console.log('Negative');
    }
    else {
        console.log('Positive');
    }
}
