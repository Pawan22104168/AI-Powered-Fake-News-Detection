from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model and TF-IDF vectorizer
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/home')
def homepage():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/detect')
def detect():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    news = request.form['news']
    news_vectorized = vectorizer.transform([news])
    prediction = model.predict(news_vectorized)[0]

    result = "Real News ✅" if prediction == 1 else "Fake News ❌"
    return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)
