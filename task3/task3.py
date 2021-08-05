import sys
import json

file1 = sys.argv[1]
file2 = sys.argv[2]

tests = json.loads(open(file1).read())
values = json.loads(open(file2).read())


def ref(d):
    for i in values["values"]:
        if i["id"] == d["id"]:
            d["value"] = i["value"]
    if "values" in d:
        for i in d["values"]:
            ref(i)


for i in tests["tests"]:
    ref(i)

with open('report.json', 'w+') as outfile:
    json.dump(tests, outfile)
