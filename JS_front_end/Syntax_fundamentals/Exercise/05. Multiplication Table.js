function solve(number) {
    let result;
    for (let i = 1; i < 11; i++) {
        result = number * i;
        console.log(`${number} X ${i} = ${result}`);
    }
}

solve(5)