# 📩 SMS Spam Detector

A machine learning project that classifies SMS messages as **Spam** or **Ham (Not Spam)** using **Naive Bayes** and natural language processing (NLP). The model is deployed as an interactive **Streamlit web app**.

---

## 🚀 Live Demo

👉 [Open App on Streamlit Cloud](https://rukum-maurya-sms-spam-detector-app-p3btdl.streamlit.app/)  


---

## 🧠 Key Features

- 🔤 Clean and preprocess raw text messages
- 🧮 Convert text into numeric vectors using `CountVectorizer`
- 🤖 Train a Naive Bayes classifier
- 📊 Evaluate accuracy, precision, recall, and F1-score
- 🌐 Deploy a live web app using **Streamlit**
- 💾 Save and load model/vectorizer using `joblib`

---

## 🗂️ Project Structure

```
text sms-spam-detector/
├── data/                        # Dataset (sms.tsv)
├── model/                       # Saved model + vectorizer
├── notebooks/
│ └── sms_spam_detector.ipynb    # EDA + training notebook
├── app.py                       # Streamlit web app
├── requirements.txt             # Dependencies for deployment
└── README.md                    # Project overview

``` 

---

## 📊 Dataset Info

- 📁 Name: `sms.tsv`
- 💬 Records: 5,574 SMS messages
- 📄 Labels: `ham`, `spam`
- 🗂️ Source: [UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection)

---

## 🛠️ How to Run the App Locally

### 1. Clone the repository

```bash
git clone https://github.com/Rukum-Maurya/sms-spam-detector.git
cd sms-spam-detector
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the app

```bash
streamlit run app.py
```


### Open in browser

```bash
Visit http://localhost:8501
```

---

## 📈 Model Performance
### Accuracy: 0.974

### Confusion Matrix:

|947  |  19  |
|----|----|
|10   | 139|


|                    | Precision | Recall                | F1-scorel          | support              | 
|--------------------|----------|------------------------|--------------------|----------------------|
| **Ham**                | 99%      | 98%                    | 98%                | 966                  |
| **Spam**              |   88%    |      93%               |       91%          |   149                |



>The model performs excellently in detecting spam with minimal false positives.
---

## 📌 Future Improvements
Use TF-IDF for improved vectorization

Add stopword removal and lemmatization

Visualize confusion matrix in app

Extend to detect email spam

---

## 🙋‍♂️ Author

**Rukum Maurya**  
🔗 [GitHub Profile](https://github.com/Rukum-Maurya)

🔗 [LinkedIn Profile](www.linkedin.com/in/rukummaurya)



---

## 📄 License
This project is licensed under the MIT License. Feel free to use, learn from, and extend it.
