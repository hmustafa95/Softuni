function solve(input) {
    let number = Number(input.shift());
    let collection = input.splice(0, number);
    let pieces = [];
    for (let i of collection) {
        let [piece, composer, key] = i.split('|');
        pieces.push({piece, composer, key});
    }

    while (input[0] != 'Stop') {
        let tokens = input.shift().split('|');
        let command = tokens[0];
        if (command == 'Add') {
            let piece1 = tokens[1];
            let composer = tokens[2];
            let key = tokens[3];
            let existingPiece = pieces.find((p) => p.piece === piece1);
            if (existingPiece) {
                console.log(`${tokens[1]} is already in the collection!`);
            }
            else {
                pieces.push({ piece: piece1, composer, key });
                console.log(`${tokens[1]} by ${composer} in ${key} added to the collection!`);
            }
        }
        else if (command == 'Remove'){
            let piece2 = tokens[1];
            let index = pieces.findIndex((p) => p.piece === piece2);
            if (index !== -1) {
                pieces.splice(index, 1);
                console.log(`Successfully removed ${tokens[1]}!`);
            }
            else {
                console.log(`Invalid operation! ${tokens[1]} does not exist in the collection.`);
            }
        }
        else if (command == 'ChangeKey') {
            let piece3 = tokens[1];
            let newKey = tokens[2];
            let index = pieces.findIndex((p) => p.piece === piece3);
            if (index !== -1) {
                pieces[index].key = newKey;
                console.log(`Changed the key of ${tokens[1]} to ${newKey}!`);
            }
            else {
                console.log(`Invalid operation! ${tokens[1]} does not exist in the collection.`);
            }
        }
    }
    for (let piece of pieces) {
        console.log(`${piece.piece} -> Composer: ${piece.composer}, Key: ${piece.key}`);
    }
}


solve([
    '3',
    'Fur Elise|Beethoven|A Minor',
    'Moonlight Sonata|Beethoven|C# Minor',
    'Clair de Lune|Debussy|C# Minor',
    'Add|Sonata No.2|Chopin|B Minor',
    'Add|Hungarian Rhapsody No.2|Liszt|C# Minor',
    'Add|Fur Elise|Beethoven|C# Minor',
    'Remove|Clair de Lune',
    'ChangeKey|Moonlight Sonata|C# Major',
    'Stop'  
  ])