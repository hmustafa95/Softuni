function solve(input) {
    for (let line of input) {
        obj = {};
        obj.name = line;
        obj.pn = line.length;
        console.log(`Name: ${obj.name} -- Personal Number: ${obj.pn}`);
    }
}
