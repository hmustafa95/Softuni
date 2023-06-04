function solve(word, sentence) {
    let sentencelower = sentence.toLowerCase();
    flag = true;
    words = sentencelower.split(' ');

    for (let oneword of words) {
        if (oneword == word) {
            console.log(word)
            flag = false
            return;
        }
    }

    if (flag) {
        console.log(`${word} not found!`);
    }
}

solve('javascript', 'JavaScript is the best programming language')