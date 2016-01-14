#!/usr/bin/env python

from pymongo import MongoClient
from datetime import datetime

client = MongoClient()
db = client.test

nodesResult = db.nodes.insert_many([
    {"id": 1, "label": '', "date": datetime.utcnow()},
    {"id": 2, "label": '', "date": datetime.utcnow()},
    {"id": 3, "label": '', "date": datetime.utcnow()},
    {"id": 4, "label": '', "date": datetime.utcnow()}
]);

edgesResult = db.edges.insert_many([
    {"to": 1, "from": 3},
    {"to": 1, "from": 2},
    {"to": 2, "from": 4}
]);
