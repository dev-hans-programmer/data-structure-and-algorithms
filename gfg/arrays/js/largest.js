// Naive approach
function findLargest(arr = []) {
   console.time('LARGEST');
   let largest = arr[0];
   for (let i = 0; i < arr.length; i++) {
      if (arr[i] > largest) {
         largest = arr[i];
      }
   }
   console.timeEnd('LARGEST');
   return largest;
}

// Optimal approach: Not efficient for higher input
function findLargestOptimal(arr = []) {
   console.time('LARGEST_OPTIMAL');
   arr.sort((a, b) => b - a);
   console.timeEnd('LARGEST_OPTIMAL');
   return arr[0];
}

const arr = Array.from({ length: 10000 }, (_, i) => i * 2);
console.log(findLargest(arr));
console.log(findLargestOptimal(arr));
