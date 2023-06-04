function solve(input) {
    let heros = [];
    for (let line of input) {
        let obj = {};
        let tokens = line.split(' / ');
        let name, level, items;
        [name, level, items] = [tokens[0], tokens[1], tokens[2]];
        obj.name = name;
        obj.level = level;
        obj.items = items.split(', ');
        heros.push(obj);
    }
    heros.sort((a, b) => a.level - b.level);

    for (let champ of heros) {
        console.log(`Hero: ${champ.name}\nlevel => ${champ.level}\nitems => ${champ.items.join(', ')}`);
    }
}