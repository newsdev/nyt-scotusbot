"""
Preloads grants and slip opinions.
Don't want to alert a bunch of grants and opinions that we
already know about.
"""
from clerk import utils as clerk_utils
from docket import grants
from docket import slipopinions

import scotusbot
from scotusbot import utils

# Preload grants.
s = grants.Load(terms=[int(clerk_utils.current_term())])
s.scrape()
utils.load_cases(scotusbot.MONGODB_DATABASE.grants, s.cases, "GRANTED", "question_url")

# Preload slip opinions.
o = slipopinions.Load(terms=[int(clerk_utils.current_term())])
o.scrape()
utils.load_cases(scotusbot.MONGODB_DATABASE.slipopinions, o.cases, "DECIDED", "opinion_pdf_url")
