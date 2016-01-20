#!/usr/bin/env python

from pymongo import MongoClient
from datetime import datetime

client = MongoClient()
db = client.test

if db.indicators.count() == 0:
    indicatorsInsertResult = db.indicators.insert_many([
        {
            "_id": "ind1",
            "value": "ind1",
            "status": "Analyzed",
            "source": [
                {
                    "name": "ETJF",
                    "instances": [
                        {
                            "date": datetime.utcnow(),
                            "reference": "sp1"
                        },
                        {
                            "date": datetime.utcnow(),
                            "reference": "sp2"
                        },
                        {
                            "date": datetime.utcnow(),
                            "reference": "sp3"
                        }
                    ]
                }
            ]
        },
        {
            "_id": "ind2",
            "value": "ind2",
            "status": "Analyzed",
            "source": [
                {
                    "name": "ETJF",
                    "instances": [
                        {
                            "date": datetime.utcnow(),
                            "reference": "sp1"
                        },
                        {
                            "date": datetime.utcnow(),
                            "reference": "sp2"
                        }
                    ]
                }
            ]
        },
        {
            "_id": "ind3",
            "value": "ind3",
            "status": "Analyzed",
            "source": [
                {
                    "name": "ETJF",
                    "instances": [
                        {
                            "date": datetime.utcnow(),
                            "reference": "sp1"
                        },
                        {
                            "date": datetime.utcnow(),
                            "reference": "sp2"
                        }
                    ]
                }
            ]
        },
        {
            "_id": "ind4",
            "value": "ind4",
            "status": "Analyzed",
            "source": [
                {
                    "name": "HF",
                    "instances": [
                        {
                            "date": datetime.utcnow(),
                            "reference": "sp2"
                        },
                        {
                            "date": datetime.utcnow(),
                            "reference": "sp3"
                        }
                    ]
                }
            ]
        },
        {
            "_id": "ind5",
            "value": "ind5",
            "status": "Analyzed",
            "source": [
                {
                    "name": "HF",
                    "instances": [
                        {
                            "date": datetime.utcnow(),
                            "reference": "sp3"
                        }
                    ]
                }
            ]
        }
    ])
