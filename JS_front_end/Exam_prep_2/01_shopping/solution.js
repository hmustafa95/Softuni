function solve(input) {
    let first = input.splice(0, 1);
    let second = first[0];
    let products = second.split('!');

    while (input[0] != 'Go Shopping!') {
        let tokens = input.shift().split(' ');
        let command = tokens[0];
        if (command === 'Urgent') {
            let item = tokens[1];
            if (!products.includes(item)) {
                products.unshift(item);
            }
        }
        else if (command === 'Unnecessary') {
            let item = tokens[1];
            if (products.includes(item)) {
                products.splice(products.indexOf(item), 1);
            }
        }
        else if (command === 'Correct') {
            let oldItem = tokens[1];
            let newItem = tokens[2];
            if (products.includes(oldItem)) {
                let index = products.indexOf(oldItem);
                products[index] = newItem;
            }
        }
        else if (command === 'Rearrange') {
            let item = tokens[1];
            if (products.includes(item)) {
                let index = products.indexOf(item);
                products.splice(index, 1);
                products.push(item);
            }
        }
    }

    console.log(products.join(', '));
}

solve((["Tomatoes!Potatoes!Bread",
"Unnecessary Milk",
"Urgent Tomatoes",
"Go Shopping!"]));