use zoo;

db.animals.dropIndexes();

db.animals.createIndex({ "type": "text", description: "text" });

db.animals.find({ $text: { $search: "Dog" } }).pretty()

// const id = ObjectId("5f8d898db645eab70f1683da")
db.animals.deleteOne({ _id: ObjectId('5f8d898db645eab70f1683db') });
// db.animals.findOne({ _id: id });
// db.animals.updateOne({ _id: id }, { $set: { name: "Princess Peach" } });