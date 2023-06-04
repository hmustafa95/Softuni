function solve(input) {
    let songs = [];
    class Song {
        constructor(typeList, name, time) {
            this.typeList = typeList;
            this.name = name;
            this.time = time;
        }
    }

    for (let i = 1; i < input.length - 1; i++) {
        let songdata = input[i].split('_');
        let typeList, name, time;
        [typeList, name, time] = [songdata[0], songdata[1], songdata[2]];
        songs.push(new Song(typeList, name, time));
    }

    if (input[input.length - 1] == 'all') {
        for (let key of songs) {
            console.log(key.name);
        }
    }
    else {
        for (let key of songs) {
            if (key.typeList == input[input.length - 1]) {
                console.log(key.name);
            }
        }
    }
}
