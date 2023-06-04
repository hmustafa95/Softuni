function solve() {
   const allButtons = Array.from(document.getElementsByClassName('add-product'));
   const textArea = document.getElementsByTagName('textarea')[0];
   const checkout = document.getElementsByClassName('checkout')[0];
   textArea.disabled = false;

   allButtons.forEach((button) => {
      button.addEventListener('click', onAdd)
   });
   
   let totalSum = 0;
   let products = [];

   function onAdd(event) {
      const parentDiv = event.target.parentElement.parentElement;
      const productName = parentDiv.querySelector('.product-title').textContent;
      const productPrice = parentDiv.querySelector('.product-line-price').textContent;

      totalSum += Number(productPrice);
      textArea.value += `Added ${productName} for ${Number(productPrice).toFixed(2)} to the cart.\n`;

      if (!products.includes(productName)) {
         products.push(productName)};
   }

   checkout.addEventListener('click', checkoutHandler);

   function checkoutHandler() {
      textArea.value += `You bought ${products.join(', ')} for ${totalSum.toFixed(2)}.`
      allButtons.forEach(button => button.disabled = true);
      checkout.disabled = true;
   }
}