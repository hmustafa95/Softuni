function solve() {
  let input = document.getElementById('text').value;
  let currentCase = document.getElementById('naming-convention').value;
  let result = document.getElementById('result');
  input = input.toLowerCase();
  
  if (currentCase === 'Pascal Case') {
    words = input.split(' ');
    for (let i = 0; i < words.length; i++) {
      words[i] = words[i].charAt(0).toUpperCase() + words[i].slice(1);
    }
    result.textContent = words.join('');
  }
  else if (currentCase === 'Camel Case') {
    words = input.split(' ');
    for (let i = 1; i < words.length; i++) {
      words[i] = words[i].charAt(0).toUpperCase() + words[i].slice(1);
    }
    result.textContent = words.join('');
  }
  else {
    result.textContent = 'Error!';
  }
}