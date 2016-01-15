#!/usr/bin/env python

from pymongo import MongoClient
from datetime import datetime

client = MongoClient()
db = client.test

if db.indicators.count() == 0:
    indicatorsInsertResult = db.indicators.insert_many([
        {
            "type": "Web",
            "value": "site",
            "status": "Analyzed",
            "source": [
                {
                    "name": "GOOG",
                    "instances": [
                        {
                            "date": datetime.utcnow(),
                            "reference": "http://google.com"
                        }
                    ]
                }
            ]
        },
        {
            "type": "Web",
            "value": "site",
            "status": "Analyzed",
            "source": [
                {
                    "name": "YHOO",
                    "instances": [
                        {
                            "date": datetime.utcnow(),
                            "reference": "http://yahoo.com"
                        },
                        {
                            "date": datetime.utcnow(),
                            "reference": "http://google.com"
                        },
                        {
                            "date": datetime.utcnow(),
                            "reference": "http://microsoft.com"
                        }
                    ]
                }
            ]
        },
        {
            "type": "Web",
            "value": "site",
            "status": "Analyzed",
            "source": [
                {
                    "name": "MSFT",
                    "instances": [
                        {
                            "date": datetime.utcnow(),
                            "reference": "http://yahoo.com"
                        },
                        {
                            "date": datetime.utcnow(),
                            "reference": "http://microsoft.com"
                        }
                    ]
                }
            ]
        }
    ])
