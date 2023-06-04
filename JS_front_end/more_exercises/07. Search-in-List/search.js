function search() {
   let result = document.getElementById('result');
   let search = document.getElementById('searchText');
   let towns = Array.from(document.getElementsByTagName('li'));
   let counter = 0;
   towns.forEach((li) => {
      li.style.textDecoration = 'none'; 
      li.style.fontWeight = '400';
   })

   for (let town of towns) {
      if (town.textContent.includes(search.value)) {
         town.style.fontWeight = 'bold';
         town.style.textDecoration = 'underline';
         counter += 1;
      }
   }

   result.textContent = `${counter} matches found`;
   search.value = '';
}
