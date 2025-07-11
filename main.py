import pickle

# Load Model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load Vectorizer
with open('tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Prediction Function
def predict_news(text):
    text = text.lower()
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)
    return "Real News" if prediction[0] == 1 else "Fake News"

# User Input
news = input("Enter News Text: ")
print(predict_news(news))
