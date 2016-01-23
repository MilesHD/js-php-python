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
                            "date": datetime(2016, 1, 22),
                            "reference": "sp1"
                        },
                        {
                            "date": datetime(2016, 1, 22),
                            "reference": "sp2"
                        },
                        {
                            "date": datetime(2016, 1, 22),
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
                            "date": datetime(2016, 1, 21),
                            "reference": "sp1"
                        },
                        {
                            "date": datetime(2016, 1, 21),
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
                            "date": datetime(2016, 1, 20),
                            "reference": "sp1"
                        },
                        {
                            "date": datetime(2016, 1, 20),
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
                            "date": datetime(2016, 1, 20),
                            "reference": "sp2"
                        },
                        {
                            "date": datetime(2016, 1, 20),
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
                            "date": datetime(2016, 1, 19),
                            "reference": "sp3"
                        }
                    ]
                }
            ]
        },
        {
            "_id": "ind6",
            "value": "ind6",
            "status": "Analyzed",
            "source": [
                {
                    "name": "HF",
                    "instances": [
                        {
                            "date": datetime(2016, 1, 18),
                            "reference": "sp4"
                        }
                    ]
                }
            ]
        }
    ])
