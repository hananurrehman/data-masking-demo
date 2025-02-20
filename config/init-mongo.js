db = db.getSiblingDB('demo_db'); // Switch to the correct database

// Create 'users' collection if it doesn't exist
if (!db.getCollectionNames().includes('users')) {
    db.createCollection('users');
}

// Insert sample users with more sensitive fields
db.users.insertMany([
    { 
        name: "Jason Bourne", 
        email: "jason@test.com", 
        ssn: "123-45-6789",
        credit_card: "4111-1111-1111-1234",
        phone: "555-123-4567",
        dob: "1978-06-15"
    },
    { 
        name: "John Wick", 
        email: "john@test.com", 
        ssn: "987-65-4321",
        credit_card: "5500-0000-0000-9876",
        phone: "555-987-6543",
        dob: "1964-09-01"
    },
    { 
        name: "Sarah Connor", 
        email: "sarah@test.com", 
        ssn: "234-56-7890",
        credit_card: "3400-123456-78901",
        phone: "555-321-7654",
        dob: "1985-12-22"
    }
], { ordered: false });
