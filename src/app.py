from pymongo import MongoClient
from flask import Flask, jsonify
from data_masking import mask_ssn
import os

app = Flask(__name__)

# MongoDB connection
mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(mongo_uri)
db = client["demo_db"]
users_collection = db["users"]

@app.route("/users", methods=["GET"])
def get_users():
    users = list(users_collection.find({}, {"_id":0}))
    masked_users = [mask_ssn(user) for user in users]
    return jsonify(masked_users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)