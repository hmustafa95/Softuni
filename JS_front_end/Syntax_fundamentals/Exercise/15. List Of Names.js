function solve(arr) {
    arr.sort();
    let counter = 0;
    for (let i = 0; i < arr.length; i++) {
        counter += 1
        console.log(`${counter}.${arr[i]}`);
    }
}
