db = db.getSiblingDB('demo_db');
db.createCollection('users');
db.users.insertMany([
    { name: "Jason Bourne", email: "jason@test.com", ssn: "123-45-6789"},
    { name: "John Wick", email: "john@test.com", ssn: "987-65-4321"}
])