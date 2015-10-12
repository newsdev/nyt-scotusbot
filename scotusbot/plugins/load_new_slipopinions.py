from clerk import utils as clerk_utils
from docket import slipopinions

import scotusbot
from scotusbot import utils

outputs = []
crontable = []
crontable.append([30, "load_slipopinions"])

def load_slipopinions():
    s = slipopinions.Load(terms=[int(clerk_utils.current_term())])
    s.scrape()

    messages = utils.load_cases(scotusbot.MONGODB_DATABASE.slipopinions, s.cases, "DECIDED", "opinion_pdf_url", alert=True)

    for message in messages:
        outputs.append([scotusbot.CHANNEL, message])
