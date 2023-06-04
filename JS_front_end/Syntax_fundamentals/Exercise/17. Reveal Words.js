function solve(words, sentence) {
    words = words.split(', ');
    sentence = sentence.split(' ');
    for (let y = 0; y < sentence.length; y++) {
        for (let i = 0; i < words.length; i++) {
            if (sentence[y].includes('*') && sentence[y].length == words[i].length) {
                sentence[y] = words[i];
            }
        }
    }
    console.log(sentence.join(' '));
}

solve('great, learning', 'softuni is ***** place for ******** new programming languages')