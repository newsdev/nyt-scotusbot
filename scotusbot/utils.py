import scotusbot

def load_cases(collection, cases, verb, detail_field, alert=False):
    """
    Reusable function for loading cases.
    Will insert new cases not yet seen in this collection.
    Returns a list of messages to be alerted to Slack.
    """
    messages = []
    for case in cases:
        if not collection.find_one({'term': case.term, 'docket': case.docket}):
            collection.insert(case.__dict__)
            if alert:
                message = "*%s: %s*\n%s\n%s" % (verb, case.docket, case.casename, getattr(case, detail_field))
                messages.append([scotusbot.CHANNEL,message])

    return messages