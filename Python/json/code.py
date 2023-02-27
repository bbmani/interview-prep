import json
from urllib.request import urlopen
# '''
#     loads - loads the string
#     load - load the json object from a file
# '''

# with open("Python\\json\\states.json", "r") as f:
#     data = json.load(f)

# for state in data["states"] : 
#     del state["area_codes"]

# with open("Python\\json\\new_states.json", "w") as wf:
#     json.dump(data, wf, indent=2, sort_keys=True)
    
with urlopen("https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json") as resource_url:
    source = resource_url.read()

json_data = json.loads(source)
print(json.dumps(json_data, indent=2))

common_powers = set()

for powers in json_data["members"]: 
    for x in powers['powers']: common_powers.add(x)

print(common_powers)

for member in json_data["members"] : 
    del member["powers"]

print(json.dumps(json_data, indent=2))

# new_json_string = json.dumps(json_data, indent=2, sort_keys=True)

# with open("Python\\json\\powers.json", "w") as wf:
#     wf.write(new_json_string)

with open("Python\\json\\powers.json", "w") as wf:
    json.dump(json_data, wf, indent=2, sort_keys=True)

# with open("Python\\json\\powers.json", "w") as wf:
#     json.dump(json_data, wf)

with open("Python\\json\\powers.json", "r") as rf:
    size_to_read = 30
    power_contents = rf.read()
    print(type(power_contents))
    json_loader = json.loads(power_contents)
    print(json_loader)
    print(type(json_loader))

with open("Python\\json\\powers.json", "r") as rf:
    new_contents = json.load(rf)
    print(new_contents)
    print(type(new_contents))