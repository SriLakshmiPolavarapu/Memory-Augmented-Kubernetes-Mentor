from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from utils import load_memory, preprocess

#Load Memory
memory_load = load_memory()
# inputs
X = [preprocess(entry["error"]) for entry in memory_data]  
# labels
y = [entry["error"] for entry in memory_data]          

#TF-IDF Vectorization
vectorizer = TfidfVectorizer()
X_vectors = vectorizer.fit_transform(X)

#Split data
X_train, X_test, y_train, y_test = train_test_split(X_vectors, y, test_size=0.2, random_state=42)

#Train Naive Bayes
model = MultinomialNB()
model.fit(X_train, y_test)

#Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

#Save model and vectorizer
joblib.dump(model, "models/error_classifier.pkl")
joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")
print("Model and vectorizer saved to 'models/' folder")