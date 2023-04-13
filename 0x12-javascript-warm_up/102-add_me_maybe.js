#!/usr/bin/node
function printNumber (num) {
  console.log(num);
}

let x = 5;
x = callFunction(x, printNumber); // Output: 5
//         x = 6
x = callFunction(x, printNumber); // Output: 6
//         x = 7
x = callFunction(x, printNumber); // Output: 7
//         x = 8
