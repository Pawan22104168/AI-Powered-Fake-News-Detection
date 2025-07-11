import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import pickle

# Load Dataset
true = pd.read_csv('True.csv')
fake = pd.read_csv('Fake.csv')

# Add Labels
true['label'] = 1
fake['label'] = 0

# Combine & Shuffle
data = pd.concat([true, fake], axis=0).sample(frac=1).reset_index(drop=True)

# Preprocessing
data['text'] = (data['title'] + " " + data['text']).str.lower()

X = data['text']
y = data['label']

# Vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_vec = vectorizer.fit_transform(X)

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

# Model Training
model = LogisticRegression()
model.fit(X_train, y_train)

print("Train Accuracy:", model.score(X_train, y_train))
print("Test Accuracy:", model.score(X_test, y_test))

print("\nClassification Report:\n")
print(classification_report(y_test, model.predict(X_test)))

# Save Model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Save Vectorizer
with open('tfidf_vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)
