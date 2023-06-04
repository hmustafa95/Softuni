function solve (input) {
    let schedule = {};
    for (let line of input) {
        let tokens = line.split(' ');
        let day = tokens[0];
        let name = tokens[1];
        if (schedule.hasOwnProperty(day)) {
            console.log(`Conflict on ${day}!`);
            continue;
        }
        schedule[day] = name;
        console.log(`Scheduled for ${day}`);
    }
    for (let key in schedule) {
        console.log(`${key} -> ${schedule[key]}`);
    }
}
