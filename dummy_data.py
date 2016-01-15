#!/usr/bin/env python

from pymongo import MongoClient
from datetime import datetime

client = MongoClient()
db = client.test

if db.indicators.count() == 0:
    indicatorsInsertResult = db.indicators.insert_many([
        {
            "type": "Website",
            "value": "Welcome to Google!",
            "status": "Analyzed",
            "source": [
                {
                    "name": "ETJF",
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
            "type": "Website",
            "value": "Welcome to Yahoo",
            "status": "Analyzed",
            "source": [
                {
                    "name": "ETJF",
                    "instances": [
                        {
                            "date": datetime.utcnow(),
                            "reference": "http://yahoo.com"
                        },
                        {
                            "date": datetime.utcnow(),
                            "reference": "http://google.com"
                        }
                    ]
                }
            ]
        },
        {
            "type": "Website",
            "value": "Welcome to Kapersky",
            "status": "Analyzed",
            "source": [
                {
                    "name": "ETJF",
                    "instances": [
                        {
                            "date": datetime.utcnow(),
                            "reference": "http://yahoo.com"
                        },
                        {
                            "date": datetime.utcnow(),
                            "reference": "http://kapersky.com"
                        }
                    ]
                }
            ]
        },
        {
            "type": "Website",
            "value": "Welcome to McAffee",
            "status": "Analyzed",
            "source": [
                {
                    "name": "HF",
                    "instances": [
                        {
                            "date": datetime.utcnow(),
                            "reference": "http://yahoo.com"
                        },
                        {
                            "date": datetime.utcnow(),
                            "reference": "http://mcaffee.com"
                        }
                    ]
                }
            ]
        },
        {
            "type": "Website",
            "value": "Welcome to McAffee/Amazon",
            "status": "Analyzed",
            "source": [
                {
                    "name": "HF",
                    "instances": [
                        {
                            "date": datetime.utcnow(),
                            "reference": "http://amazon.com"
                        },
                        {
                            "date": datetime.utcnow(),
                            "reference": "http://mcaffee.com"
                        }
                    ]
                }
            ]
        },
        {
            "type": "Website",
            "value": "Welcome to Youtube",
            "status": "Analyzed",
            "source": [
                {
                    "name": "HF",
                    "instances": [
                        {
                            "date": datetime.utcnow(),
                            "reference": "http://amazon.com"
                        },
                        {
                            "date": datetime.utcnow(),
                            "reference": "http://youtube.com"
                        }
                    ]
                }
            ]
        },
        {
            "type": "Website",
            "value": "Welcome to Amazon",
            "status": "Analyzed",
            "source": [
                {
                    "name": "HF",
                    "instances": [
                        {
                            "date": datetime.utcnow(),
                            "reference": "http://google.com"
                        },
                        {
                            "date": datetime.utcnow(),
                            "reference": "http://amazon.com"
                        }
                    ]
                }
            ]
        }
    ])
