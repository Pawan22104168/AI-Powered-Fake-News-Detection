# FakeNewsAI

![Logo](https://img.icons8.com/ios-filled/40/22c55e/news.png)

**AI-Powered Fake News Detection**

Instantly verify the authenticity of news articles and headlines using advanced machine learning. Protect yourself and your organization from misinformation with just one click.

---

## 🚀 Features
- **AI-Powered Detection:** State-of-the-art machine learning analyzes news content for authenticity in seconds.
- **Real-time Results:** Get instant feedback on news articles and headlines, anytime, anywhere.
- **Privacy & Security:** Your news is processed securely and never stored. 100% privacy guaranteed.
- **Global Coverage:** Analyze news in multiple languages from sources around the world.
- **Modern UI:** Clean, responsive, and professional web interface.

---

## 🖥️ Demo

![FakeNewsAI Demo Screenshot](https://img.icons8.com/ios-filled/150/22c55e/news.png)

Try it locally:
```
http://127.0.0.1:5000/home
```

---

## 📂 Folder Structure
```
News_detection_final/
├── app.py                  # Main Flask app
├── train_model.py          # Model training script
├── model.pkl               # Trained ML model
├── tfidf_vectorizer.pkl    # Saved TF-IDF vectorizer
├── requirements.txt        # Python dependencies
├── static/
│   └── style.css           # Main stylesheet
├── templates/
│   ├── home.html           # Home page
│   ├── about.html          # About page
│   ├── contact.html        # Contact page
│   └── index.html          # Detect page
└── ...
```

---

## ⚙️ Setup & Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/FakeNewsAI.git
   cd FakeNewsAI/News_detection_final
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   pip install flask
   ```
3. **(Optional) Train your own model:**
   - Place your `True.csv` and `Fake.csv` datasets in the project folder.
   - Run:
     ```sh
     python train_model.py
     ```
   - This will generate `model.pkl` and `tfidf_vectorizer.pkl`.
4. **Run the app:**
   ```sh
   cd "News detection final"
   python app.py
   ```
5. **Open in your browser:**
   - Home:   `http://127.0.0.1:5000/home`
   - Detect: `http://127.0.0.1:5000/detect`
   - About:  `http://127.0.0.1:5000/about`
   - Contact: `http://127.0.0.1:5000/contact`

---

## 📝 Usage
- **Home:** Learn about the platform and its features.
- **Detect:** Paste a news headline and article to check authenticity.
- **About:** Understand the mission, technology, and privacy approach.
- **Contact:** Reach out for support or questions.

---

## 🛠️ Tech Stack
- **Frontend:** HTML5, CSS3 (Inter font, responsive design)
- **Backend:** Python, Flask
- **ML:** scikit-learn, pandas, numpy

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License
[MIT](LICENSE)

---

## 📬 Contact
For support or questions, email: [your@email.com](mailto:your@email.com) 
