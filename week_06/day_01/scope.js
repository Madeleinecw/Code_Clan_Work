// // var secretsFunction = function() {
// //     var pinCode = [0, 0, 0, 0];
// //     console.log('pinCode inside fucntion', pinCode)
// // }

// // // secretsFunction();

// // var filterNamesByFirstLetter = function(names, letter) {
// //     var filteredNames = [];
// //     for (var name of names) {
// //         if (name[0] === letter) {
// //             filteredNames.push(name);
// //         }
// //     }
// //     return filteredNames;
// // }

// // console.log(filterNamesByFirstLetter(['Holly', 'Mark', 'Simon', 'John', 'Hunter'], 'H'));

// let isItFive = function(num) {
//     let result;
//     if (num === 5) {
//         result = true;
//     } else {
//         result = false;
//     }
//     return result;
// }

// console.log(isItFive(4));

let calculateEnergy = function(mass) {
    let speedOfLight = 299792458;
    return mass * speedOfLight ** 2;
}

console.log("My Energy", calculateEnergy(83));