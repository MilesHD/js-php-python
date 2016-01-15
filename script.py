
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
            "type": 1,
            "value": 1,
            "status": 1,
            "source.name": 1,
            "source.instances.date": 1,
            "source.instances.reference": 1}):
    indicators.append(ind)

########### DATA TRANSFORMATION ##########

nodes = []
edges = []
references = []

# Extract References and create nodes
for ind in indicators:
    for src in ind["source"]:
        for inst in src["instances"]:
            references.append(inst["reference"])
            node = {
                "id": str(ind["_id"]),
                "type": ind["type"],
                "value": ind["value"],
                "reference": inst["reference"]
            }
            nodes.append(node)

# Create Edges
for ind in indicators:
    for src in ind["source"]:
        for inst in src["instances"]:
            for ref in references:
                if "reference" in inst and inst["reference"] in references and {"from": str(ind["_id"]), "to": ref} not in edges:
                    edges.append({"from": str(ind["_id"]), "to": ref})


nodes = JSONEncoder().encode(nodes)
edges = JSONEncoder().encode(edges)

########### DATA TRANSMISSION ##########

# print is a thin wrapper that formats inputs and
# calls the write function on a given object (default: sys.stdout)
print nodes + "SPLIT" + edges
