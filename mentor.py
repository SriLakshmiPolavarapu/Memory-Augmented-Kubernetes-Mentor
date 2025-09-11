import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


with open("data/memory.json", "r") as f:
    data = json.load(f)
    
errors = [entry["error"] for entry in data]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(errors)

user_input = input("Enter the error you are getting : ")    

user_vec = vectorizer.transform([user_input])

similarities = cosine_similarity(user_vec, X).flatten()

best_idx = similarities.argmax()
best_score = similarities[best_idx]

if best_score > 0.2:
    entry = data[best_idx]
    print(entry["error"])
    print(" ---> Explanation of the error : ", entry["cause"])
    for s in entry["solutions"]:
            print(s)
    for cmd in entry["next_steps"]:
            print(cmd)
    print(" ---> Here is the suggested YAML : ", entry["snippet"]) 
else:
    print(" ---> No match found")


        
        

