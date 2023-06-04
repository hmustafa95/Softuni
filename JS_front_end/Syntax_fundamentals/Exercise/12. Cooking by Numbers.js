function solve(num, action1, action2, action3, action4, action5) {
    let number = parseInt(num);
    if (action1 == 'chop') {
        number /= 2;
        console.log(number);
    }
    else if (action1 == 'dice') {
        number = Math.sqrt(number);
        console.log(number);
    }
    else if (action1 == 'spice') {
        number += 1;
        console.log(number);
    }
    else if (action1 == 'bake') {
        number *= 3;
        console.log(number);
    }
    else if (action1 == 'fillet') {
        number -= number * 0.2;
        console.log(number);
    }
    if (action2 == 'chop') {
        number /= 2;
        console.log(number);
    }
    else if (action2 == 'dice') {
        number = Math.sqrt(number);
        console.log(number);
    }
    else if (action2 == 'spice') {
        number += 1;
        console.log(number);
    }
    else if (action2 == 'bake') {
        number *= 3;
        console.log(number);
    }
    else if (action2 == 'fillet') {
        number -= number * 0.2;
        console.log(number);
    }
    if (action3 == 'chop') {
        number /= 2;
        console.log(number);
    }
    else if (action3 == 'dice') {
        number = Math.sqrt(number);
        console.log(number);
    }
    else if (action3 == 'spice') {
        number += 1;
        console.log(number);
    }
    else if (action3 == 'bake') {
        number *= 3;
        console.log(number);
    }
    else if (action3 == 'fillet') {
        number -= number * 0.2;
        console.log(number);
    }
    if (action4 == 'chop') {
        number /= 2;
        console.log(number);
    }
    else if (action4 == 'dice') {
        number = Math.sqrt(number);
        console.log(number);
    }
    else if (action4 == 'spice') {
        number += 1;
        console.log(number);
    }
    else if (action4 == 'bake') {
        number *= 3;
        console.log(number);
    }
    else if (action4 == 'fillet') {
        number -= number * 0.2;
        console.log(number);
    }
    if (action5 == 'chop') {
        number /= 2;
        console.log(number);
    }
    else if (action5 == 'dice') {
        number = Math.sqrt(number);
        console.log(number);
    }
    else if (action5 == 'spice') {
        number += 1;
        console.log(number);
    }
    else if (action5 == 'bake') {
        number *= 3;
        console.log(number);
    }
    else if (action5 == 'fillet') {
        number -= number * 0.2;
        console.log(number);
    }
}

solve('32', 'chop', 'chop', 'chop', 'chop', 'chop')