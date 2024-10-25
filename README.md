# Flask MongoDB Data Masking Demo

This project is a simple Python application demonstrating data masking while fetching data from a MongoDB instance. It is built with Flask and connected to MongoDB using Docker containers. The data is fetched from MongoDB and masked before being returned via a Flask API.

## Project Setup

1. **Install Docker**: Make sure you have Docker installed on your system. You can download it from [Docker's official website](https://www.docker.com/).

2. **Clone the Repository**: Clone this repository to your local machine.
```bash
git clone https://github.com/your-username/flask-mongodb-data-masking.git
cd flask-mongodb-data-masking
```
3. **Ensure the Required Files Exist**:
- `docker-compose.yml`: Defines services for MongoDB and the Flask app.
- `app.py`: The Flask API that connects to MongoDB and masks sensitive data.
- `config/init-mongo.js`: MongoDB initialization script (for setting up initial data).
- `src/`: Directory where the Flask application and other code reside.

## Docker Setup
The project uses Docker Compose to create and manage the containers for both the MongoDB database and the Flask application.

**Steps to Run the Project**:

1. **Build and Run Containers**: Ensure Docker is running, then use the following command to build and start the services:
```bash
docker-compose up --build
```
2. **Access the Flask Application**: Once the containers are up, access the Flask app via:
```bash
http://localhost:5001
```

The default port is 5001, but you can change it in `docker-compose.yml` if needed.

Check MongoDB: MongoDB will be accessible at `localhost:27017`. The MongoDB root username is `root`, and the password is `example` (set in `docker-compose.yml`).

## MongoDB Initialization
An initial MongoDB setup script, `config/init-mongo.js`, is used to populate the database with some default data. 

## Flask API Endpoints
The Flask API exposes the following endpoint:

`GET /users`: Fetch all users from MongoDB. Sensitive information (like ssn) will be masked before being returned.


## Technologies Used
- Python: Backend logic using Flask.
- MongoDB: A NoSQL database for storing user data.
- Docker: Containerization for both the Flask app and MongoDB instance.
- PyMongo: MongoDB driver for Python.
