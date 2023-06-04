function oddeven(number) {
    let numString = number.toString();
    let oddsum = 0;
    let evensum = 0;
    for (let i = 0; i < numString.length; i++) {
        let digit = parseInt(numString[i]);
        if (digit % 2 === 0) {
            evensum += digit;
        }
        else {
            oddsum += digit;
        }
    }
    console.log(`Odd sum = ${oddsum}, Even sum = ${evensum}`);
}
