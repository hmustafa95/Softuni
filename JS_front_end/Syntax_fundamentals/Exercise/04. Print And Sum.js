function solve(start, end) {
    let result = 0;
    let list = ''
    for (let i = start; i < end + 1; i++) {
        result += i;
        list += `${i} `
    }
    console.log(list);
    console.log(`Sum: ${result}`);
}

solve(5, 10)