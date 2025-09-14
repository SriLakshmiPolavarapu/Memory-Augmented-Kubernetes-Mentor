import joblib
from utils import load_memory, preprocess

memory_data = load_memory()
model = joblib.load("models/error_classifier.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

user_input = input("Enter the Kubernetes error you are getting: ")
user_input_processed = preprocess(user_input)
user_vec = vectorizer.transform([user_input_processed])

predicted_category = model.predict(user_vec)[0]
probability = model.predict_proba(user_vec).max()

threshold = 0.3
if probability >= threshold:
    entry = next((e for e in memory_data if e["error"] == predicted_category), None)
    if entry:
        print("\n--- Error Details ---")
        print("Error:", entry["error"])
        print("Explanation:", entry["cause"])
        print("\nPossible Fixes:")
        for s in entry["solutions"]:
            print("-", s)
        print("\nNext Steps:")
        for cmd in entry["next_steps"]:
            print("-", cmd)
        print("\nSuggested YAML snippet:\n", entry["snippet"])
else:
    print("\nNo confident match found. You may need to check logs or YAML manually.")
