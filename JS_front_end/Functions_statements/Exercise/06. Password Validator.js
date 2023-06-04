function validator(pass) {
    flag1 = false;
    flag2 = false;
    flag3 = false;

    if (pass.length >= 6 && pass.length <= 10) {
        flag1 = true;
    }
    else {
        console.log("Password must be between 6 and 10 characters");
    }

    if (/^[a-zA-Z0-9]+$/.test(pass)) {
        flag2 = true;
    }
    else {
        console.log("Password must consist only of letters and digits");
    }

    let counter = 0;
    for (let i = 0; i < pass.length; i++) {
        digit = parseInt(pass[i]);
        if (digit) {
            counter += 1;
        }
    }

    if (counter >= 2) {
        flag3 = true;
    }
    else {
        console.log("Password must have at least 2 digits");
    }

    if (flag1 && flag2 && flag3) {
        console.log("Password is valid");
    }
}
