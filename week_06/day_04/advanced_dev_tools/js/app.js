document.addEventListener("DOMContentLoaded", function() {
    // ...
    const fruits = ["apple", "orange", "banana"];
    console.table(fruits);

    const person = {
        name: "Jane",
        age: 40
    };
    console.table(person);
});

document.addEventListener("DOMContentLoaded", function() {
    debugger;
    let number1 = 5;
    number1 += 10;
    const number2 = 20 + number1;
    const number3 = number2 / 10;
});