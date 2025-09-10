import json

with open("data/memory.json", "r") as f:
    data = json.load(f)
    

user_input = input("Enter the error you are getting : ")    

for entry in data:
    if entry["error"].lower() in user_input.lower():
        print("Explanation of the error : ", entry["cause"])
        print("Here are the possible fixes : ")
        for s in entry["solutions"]:
            print(s)
        for cmd in entry["next_steps"]:
            print(cmd)
        print("Here is the suggested YAML : ", entry["snippet"])
        break   
    else:
        print("No match found")

