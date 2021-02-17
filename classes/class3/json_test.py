import json

output = {
    "mean": 12.34,
    "mode": 2,
    "median": 7
}

with open('output.json', 'w') as f:
    json.dump(output, f)