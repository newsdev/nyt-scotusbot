import os

from pymongo import MongoClient

CHANNEL = os.environ.get("SCOTUSBOT_SLACK_CHANNEL", None)
MONGODB_CLIENT = MongoClient(os.environ.get('SCOTUSBOT_MONGO_URL', 'mongodb://localhost:27017/'))
MONGODB_DATABASE = MONGODB_CLIENT.campfinbot