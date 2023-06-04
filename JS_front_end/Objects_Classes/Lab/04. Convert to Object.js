function solve(somestring) {
    let person = JSON.parse(somestring);
    let entries = Object.entries(person);

    for (let [key, value] of entries) {
        console.log(`${key}: ${value}`);
    }
}
