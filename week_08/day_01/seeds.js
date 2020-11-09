use zoo;

db.dropDatabase();

db.animals.insertMany([{
        name: "Peach",
        type: "Cat"
    },
    {
        name: "Max",
        type: "Dog",
        age: 13
    },
])