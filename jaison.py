import json

#Convert from Json to Python

x='{"name":"John", "age":30, "city":"New York"}'

y=json.loads(x)

print(y["age"])

#Convert from Python to Json

y='{"name":"John", "age":30, "city":"New York"}'

z=json.dumps(x)

print(y)
print(json.dumps({"name":"John", "age":30, "city":"New York"}))
print(json.dumps(["apple","bananas"]))