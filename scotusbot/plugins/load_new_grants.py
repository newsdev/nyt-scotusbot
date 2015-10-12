from clerk import utils as clerk_utils
from docket import grants

import scotusbot
from scotusbot import utils

outputs = []
crontable = []
crontable.append([30, "load_grants"])

def load_grants():
    s = grants.Load(terms=[int(clerk_utils.current_term())])
    s.scrape()

    messages = utils.load_cases(scotusbot.MONGODB_DATABASE.grants, s.cases, "GRANTED", "question_url", alert=True)

    for message in messages:
        outputs.append([scotusbot.CHANNEL, message])