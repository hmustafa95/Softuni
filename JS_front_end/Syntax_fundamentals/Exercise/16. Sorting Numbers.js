function sortAlternately(arr) {
    // Sort the array in ascending order
    arr.sort(function(a, b) {
      return a - b;
    });
  
    // Initialize two pointers
    let i = 0;
    let j = arr.length - 1;
  
    // Initialize the result array
    const result = new Array(arr.length);
  
    // Alternate between adding the smallest and largest element
    for (let k = 0; k < arr.length; k++) {
      if (k % 2 === 0) {
        result[k] = arr[i];
        i++;
      } else {
        result[k] = arr[j];
        j--;
      }
    }
  
    return result;
}