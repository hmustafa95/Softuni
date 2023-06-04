function solve(speed, area) {
    let result = 0;
    let limit = 0;
    switch (area) {
        case 'motorway': limit = 130; break;
        case 'interstate': limit = 90; break;
        case 'city': limit = 50; break;
        case 'residential': limit = 20; break;
    }

    result = speed - limit;
    let status = '';
    if (result<=20) {
        status = 'speeding';
    }
    else if (result>20 && result<=40) {
        status = 'excessive speeding';
    }
    else {
        status = 'reckless driving';
    }

    if (speed <= limit) {
        console.log(`Driving ${speed} km/h in a ${limit} zone`);
    }
    else {
        console.log(`The speed is ${result} km/h faster than the allowed speed of ${limit} - ${status}`);
    }
}
