function solve(fruit, grams, price) {
    let kgs = grams / 1000;
    let result = kgs * price;
    console.log(`I need $${result.toFixed(2)} to buy ${kgs.toFixed(2)} kilograms ${fruit}.`);
}

solve('orange', 2500, 1.80)