import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError

with open('EndPoint.json') as f:
    document = json.load(f)

with open('squema1.json') as f:
    schema = json.load(f)

try:
    validate(instance=document, schema=schema)
    print("perfecto")
except ValidationError as e:
    print(f"{e.message}")
