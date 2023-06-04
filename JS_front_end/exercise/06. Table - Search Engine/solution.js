function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      let searchField = document.getElementById('searchField');
      let field = Array.from(document.querySelectorAll('tbody td'));
      field.forEach(el => el.parentElement.removeAttribute('class'));
      field
      .filter(el => el.textContent.toLowerCase().includes(searchField.value.toLowerCase()) && searchField.value !== '')
      .forEach(el => el.parentElement.className = 'select');
      searchField.value = '';
   }
}