function solve(num, type, day) {
    let result;
    let price;
    let discount;
    switch (type) {
      case 'Students':
        switch (day) {
          case 'Friday':
            price = 8.45;
            break;
          case 'Saturday':
            price = 9.80;
            break;
          case 'Sunday':
            price = 10.46;
            break;
        }
        result = price * num;
        break;
      case 'Business':
        switch (day) {
          case 'Friday':
            price = 10.90;
            break;
          case 'Saturday':
            price = 15.60;
            break;
          case 'Sunday':
            price = 16;
            break;
        }
        result = price * num;
        if (num >= 100) {
          discount = price * 10;
          result -= discount;
        }
        break;
      case 'Regular':
        switch (day) {
          case 'Friday':
            price = 15;
            break;
          case 'Saturday':
            price = 20;
            break;
          case 'Sunday':
            price = 22.50;
            break;
        }
        result = price * num;
        if (num >= 10 && num <= 20) {
          discount = result * 0.05;
          result -= discount;
        }
        break;
    }
    if (type === 'Students' && num >= 30) {
      discount = result * 0.15;
      result -= discount;
    }
    console.log(`Total price: ${result.toFixed(2)}`);
 }