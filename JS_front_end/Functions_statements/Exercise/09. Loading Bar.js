function bar(num) {
    if (num == 100) {
        console.log('100% Complete!\n[%%%%%%%%%%]');
    }
    else {
        times = 10 - num
        loading = '[' + '%'.repeat(num) + '.'.repeat(times) + ']';
        console.log(`${num}% ${loading}\nStill loading...`);
    }
}

bar(30)

function loadingBar(number) {
    let bar = '[..........]'

    if (number == 100) {
        console.log('100% Complete!')
    } else {
        for (let i = 0; i < number; i+=10) {
            bar = bar.replace('.', '%')
        }
        console.log(`${number}% ${bar}`);
        console.log('Still loading...');  
    }
}