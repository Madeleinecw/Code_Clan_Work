// //named function declarations

// function sayHello(name) {
//     return `Hello ${name}`;
// }

// console.log("sayHello message:", sayHello("Maddie"));

// //anonymous function expressions - not hoisted like named functions
// var add = function(firstNumber, secondNumber) {
//     return firstNumber + secondNumber
// }

// console.log("1 + 3 with add:", add(1, 3))

// // Declare a named function that takes an array of numbers, and returns the sum, or total, of all of the numbers in the array.
// // Define an anonymous function expression that takes two arguments:
// // an object, for example, { name: 'Wojtek', age: 30 }
// // a string, for exmaple, 'name'
// // Your function should return true if the given string is a key on the given object and false if the object does not have a key that matches the string. Store this function in an appropriately named variable to invoke it.

// function addArray(numbers) {
//     var total = 0;
//     for (number of numbers) {
//         total += number;
//     }
//     return total;
// }

// console.log(addArray([12, 1, 1, 1]));

// var keyCheck = function(details) {
//     if (details.name == true);
//     console.log("True")
// }

// console.log(keyCheck({ name: 'Wojtek', age: 30 }))

//arrow functions - a type of anonymous function

var multiply = (firstNumber, secondNumber) => {
    return firstNumber * secondNumber;
}

console.log(multiply(2, 3));