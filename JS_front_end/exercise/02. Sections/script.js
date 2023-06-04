function create(words) {
   let parentDiv = document.getElementById('content');

   for (let word of words) {
      let div = document.createElement('div');
      let p = document.createElement('p');
      p.textContent = word;
      p.style.display = 'none';
      div.appendChild(p);
      div.addEventListener('click', function(e) {
         e.target.children[0].style.display = 'block';
      });
      parentDiv.appendChild(div);
   }
}