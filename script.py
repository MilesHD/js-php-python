
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

# Instantiate singleton to use throughout program
jsonEncoder = JSONEncoder()

# Attempt to retrieve arguments passed in with program call
try:
    indicator_id = sys.argv[1]
    days_back = int(sys.argv[2])
    sources = sys.argv[3].split(',')
    links_only = sys.argv[4]
except IndexError:
    print "ERROR: Invalid arguments"
    sys.exit(0)

# Connect to Local MongoDB Instance
client = MongoClient()
db = client.test

nodes = []
edges = []
references = []
query1_indicators = []
query2_indicators = []

########### QUERY 1 ##########

for ind in db.indicators.find(
        filter={"_id": indicator_id}, 
        projection={
            "value": 1,
            "status": 1,
            "source.name": 1,
            "source.instances.date": 1,
            "source.instances.reference": 1}):
    query1_indicators.append(ind)

# Check if indicator_id exists
# If yes, add indicator node
if (len(query1_indicators) > 0):
    nodes.append({
        "id": indicator_id,
        "type": "indicator",
        "label": indicator_id 
    })
else:
    print "ERROR: Invalid Indicator Id"
    sys.exit(0)
    
# Extract References and create nodes
for ind in query1_indicators:
    for src in ind["source"]:
        for inst in src["instances"]:
            references.append(inst["reference"])
            node = {
                "id": str(inst["reference"]),
                "type": "reference",
                "label": inst["reference"],
                # Development
                "source": src["name"]
            }
            nodes.append(node)

# Create Edges
for ind in query1_indicators:
    for src in ind["source"]:
        for inst in src["instances"]:
            for ref in references:
                if "reference" in inst and inst["reference"] in references and {"from": str(ind["_id"]), "to": ref} not in edges:
                    edges.append({"from": str(ind["_id"]), "to": ref})

########### QUERY 2 ##########

dt = datetime.datetime.utcnow() - datetime.timedelta(days=days_back)
for ind in db.indicators.find(
        filter={
            "status": "Analyzed",
            "source.instances": {
                "$elemMatch": {
                    "date": {"$gt": dt},
                    "reference": {"$in": references}
                }
            }
        }, 
        projection={
            "value": 1,
            "status": 1,
            "source.name": 1,
            "source.instances.date": 1,
            "source.instances.reference": 1}):
    query2_indicators.append(ind)

# Create nodes
for ind in query2_indicators:
    for src in ind["source"]:
        for inst in src["instances"]:
            # Only create nodes for our requested sources
            if (src["name"] in sources):
                node = {
                    "id": str(ind["_id"]),
                    "type": "indicator",
                    "label": ind["value"],
                }
                if (node not in nodes):
                    nodes.append(node)

# Create edges
for ind in query2_indicators:
    for src in ind["source"]:
        for inst in src["instances"]:
            for ref in references:
                # Only create edges for our requested sources
                if (src["name"] in sources):
                    edge = {
                        "from": str(ind["_id"]),
                        "to": ref
                    }
                    if inst["reference"] == ref and edge not in edges:
                        edges.append(edge)

# Filter indicators that are only connected to one reference
if links_only == "yes":
    node_edges = {}
    for edge in edges:
        # First occurnce of indicator
        if edge['from'] not in node_edges:
            node_edges[edge['from']] = 1
        else:
            node_edges[edge['from']] += 1
    
    # Retrieve all the keys from node_edges list that had a value greater than 1, as a list
    link_node_names = filter(lambda x: node_edges[x] > 1, node_edges)
    # Filter nodes to include only node id's with more than one link, and is of type 'indicator'
    nodes = filter(lambda x: x['type'] == 'reference' or x['id'] in link_node_names, nodes)
    # Filter edges to include only from id's with more than one link
    edges = filter(lambda x: x['from'] in link_node_names, edges)

########### DATA TRANSMISSION ##########

# Serialize nodes and edges by encoding to JSON
nodes = jsonEncoder.encode(nodes)
edges = jsonEncoder.encode(edges)

# print is a thin wrapper that formats inputs and
# calls the write function on a given object (default: sys.stdout)
print nodes + "SPLIT" + edges
