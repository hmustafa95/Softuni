function solve(input) {
    let addressbook = {};
    for (let line of input) {
        let tokens = line.split(':');
        let name = tokens[0];
        let address = tokens[1];
        addressbook[name] = address;
    }
    const sortedJson = Object.fromEntries(Object.entries(addressbook).sort((a, b) => a[0].localeCompare(b[0])));
    for (let key in sortedJson) {
        console.log(`${key} -> ${sortedJson[key]}`);
    }
}
