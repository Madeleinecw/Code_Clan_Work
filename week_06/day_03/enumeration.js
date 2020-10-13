const myNumbers = [1, 2, 3, 4, 5]

myNumbers.forEach((number, index) => [
    console.log(`This is number ${number} at index position ${index}`)
]);

const getEvens = function(numbers) {
    const result = [];
    numbers.forEach((number) => {
        if (number % 2 === 0) {
            result.push(number)
        }
    });
    return result;
}

console.log(getEvens(myNumbers));

const sumElements = function(numbers) {
    let result = 0;
    numbers.forEach((number) => {
        result += number
    });
    return result
};

console.log(sumElements(myNumbers));