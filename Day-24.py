import json

# Dictionary
print(json.dumps({"name": "John", "age": 30, "city": "New York"}))

# List conversion to Array
print(json.dumps(['Welcome', "to", "BestEnlist"]))

# Tuple conversion to Array
print(json.dumps(("Welcome", "to", "BeatEnlist")))

# String conversion to String
print(json.dumps("Hi Ketan"))

# Int conversion to Number
print(json.dumps(123))

# Float conversion to Number
print(json.dumps(23.572))

# Boolean conversion to their respective values
print(json.dumps(True))
print(json.dumps(False))

# None value to null
print(json.dumps(None))