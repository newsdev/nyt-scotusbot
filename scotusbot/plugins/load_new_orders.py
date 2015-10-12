from clerk import utils as clerk_utils
from docket import orders

import scotusbot
from scotusbot import utils

outputs = []
crontable = []
crontable.append([30, "load_orders"])

def load_orders():
    o = orders.Load(terms=[int(clerk_utils.current_term())])
    o.scrape()

    collection = scotusbot.MONGODB_DATABASE.orders

    for order in o.orders:
        if not collection.find_one({'term': order.term, 'orders_pdf_url': order.orders_pdf_url}):
            collection.insert(order.__dict__)
            message = "*ORDERS*\n%s" % order.orders_pdf_url
            outputs.append([scotusbot.CHANNEL,message])