
import json
import sys
from pymongo import MongoClient
from bson import ObjectId

# Encode BSON specific values into JSON values
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

# Connect to Local MongoDB Instance
client = MongoClient()
db = client.test

# Retrieve Nodes
nodes = []
for node in db.nodes.find():
    nodes.append(node)

# Retrieve Edges
edges = []
for edge in db.edges.find():
    edges.append(edge)

jsonNodes = JSONEncoder().encode(nodes)
jsonEdges = JSONEncoder().encode(edges)

# To pass two JSON collections as 1 string,
# will be split by client
result = jsonNodes + "split" + jsonEdges

# print is a thin wrapper that formats inputs and
# calls the write function on a given object (default: sys.stdout)
print result
