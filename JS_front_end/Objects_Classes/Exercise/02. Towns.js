function solve(input) {
    obj = {};
    for (let line of input) {
        let tokens = line.split(' | ');
        let town, latitude, longitude;
        [town, latitude, longitude] = [tokens[0], Number(tokens[1]).toFixed(2), Number(tokens[2]).toFixed(2)];
        obj.town = town;
        obj.latitude = latitude;
        obj.longitude = longitude;
        console.log(obj);
    }
}
