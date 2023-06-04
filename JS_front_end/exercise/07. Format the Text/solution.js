function solve() {
  let text = document.getElementById('input');
  let textArr = text.value.split('.').filter(s => s !== '');
  let result = document.getElementById('output');

  while(textArr.length > 0) {
    let sentences = textArr.splice(0, 3).join('. ') + '.';
    let p = document.createElement('p');
    p.textContent = sentences;
    result.appendChild(p);
  }
}