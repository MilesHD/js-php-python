
import json
import sys

try:
    name = sys.argv[1]
    result = name 
except:
    result =  "No name argument given"

nodes = [
    {"id": 1, "label": ''},
    {"id": 2, "label": ''},
    {"id": 3, "label": ''},
    {"id": 4, "label": ''}
]

edges = [
    {"to": 1, "from": 3},
    {"to": 1, "from": 2},
    {"to": 2, "from": 4}
]

jsonNodes = json.dumps(nodes)
jsonEdges = json.dumps(edges)


# To pass two JSON collections as 1 string,
# will be split by client
result = jsonNodes + "split" + jsonEdges

# print is a thin wrapper that formats inputs and
# calls the write function on a given object (default: sys.stdout)
print result
# print edges
