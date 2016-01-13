#!/usr/bin/env python

from pymongo import MongoClient

client = MongoClient()
db = client.test

nodesResult = db.nodes.insert_many([
    {"id": 1, "label": ''},
    {"id": 2, "label": ''},
    {"id": 3, "label": ''},
    {"id": 4, "label": ''}
]);

edgesResult = db.edges.insert_many([
    {"to": 1, "from": 3},
    {"to": 1, "from": 2},
    {"to": 2, "from": 4}
]);
