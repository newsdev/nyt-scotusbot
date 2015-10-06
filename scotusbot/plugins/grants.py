import humanize
import json
import os
import requests
import time
import os
import random
from sets import Set

from clerk import utils as clerk_utils
from docket import grants
from pymongo import MongoClient

outputs = []
crontable = []
crontable.append([30, "load_grants"])

CHANNEL = os.environ.get("SCOTUSBOT_SLACK_CHANNEL", None)
HOST = os.environ.get('SCOTUSBOT_MONGO_URL', 'mongodb://localhost:27017/')
client = MongoClient(HOST)
db = client.scotusbot
collection = db.grants

def load_grants():
    s = grants.Load(terms=[int(clerk_utils.current_term())])
    s.scrape()

    for case in s.cases:
        if not collection.find_one({'casename': case.casename}):
            collection.insert_one(case.__dict__)
            message = "Added *%s (%s)* to the docket." % (case.casename, case.docket)
            outputs.append([CHANNEL,message])
