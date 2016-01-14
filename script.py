
########### SETUP AND CONFIGURATION ##########

import json
import sys
from pymongo import MongoClient
from bson import ObjectId
import datetime

# Encode BSON specific values into JSON values
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId) or isinstance(o, datetime.date):
            return str(o)
        return json.JSONEncoder.default(self, o)

# Connect to Local MongoDB Instance
client = MongoClient()
db = client.test


########### DATA RETRIEVAL ##########

indicators = []
for ind in db.indicators.find(
        filter={}, 
        projection={
            "status": 1,
            "source.name": 1,
            "source.instances.date": 1,
            "source.instances.reference": 1}):
    indicators.append(ind)

########### DATA TRANSFORMATION ##########
nodes = []
edges = []
count = 0

for ind in indicators:
    for src in ind["source"]:
        for inst in src["instances"]:
            node = {
                "id": count,
                "type": "indicator",
                "reference": inst['reference']
            }
            nodes.append(node)
            count += 1

result = JSONEncoder().encode(nodes)

########### DATA TRANSMISSION ##########

# print is a thin wrapper that formats inputs and
# calls the write function on a given object (default: sys.stdout)
print result
