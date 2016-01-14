#!/usr/bin/env python

from pymongo import MongoClient
from datetime import datetime

client = MongoClient()
db = client.test

if db.indicators.count() == 0:
    indicatorsInsertResult = db.indicators.insert_many([
        {
            "status": "Analyzed",
            "source": [
                {
                    "name": "DSIE",
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
            "status": "Analyzed",
            "source": [
                {
                    "name": "DSIE",
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
            "status": "Analyzed",
            "source": [
                {
                    "name": "GE",
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
