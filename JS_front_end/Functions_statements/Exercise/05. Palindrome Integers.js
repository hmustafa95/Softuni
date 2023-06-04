function palindrome(arr) {
    for (let i = 0; i < arr.length; i++) {
        str = arr[i].toString();
        reversedStr = str.split('').reverse().join('');
        if (str == reversedStr) {
            console.log('true');
        }
        else {
            console.log('false');
        }
    }
}