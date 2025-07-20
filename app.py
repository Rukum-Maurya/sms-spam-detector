import streamlit as st
import joblib
import string
import re

# Load saved model and vectorizer
model = joblib.load("model/spam_classifier_model.joblib")
vectorizer = joblib.load("model/vectorizer.joblib")

# Text cleaning function (same as used during training)
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.strip()

# Streamlit UI
st.set_page_config(page_title="SMS Spam Detector", page_icon="📩")
st.title("📩 SMS Spam Classifier")
st.markdown("Type a message below to check if it's **Spam** or **Ham**.")

# Input box
user_input = st.text_area("Enter SMS message here:")

# Predict button
if st.button("🔍 Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        cleaned = clean_text(user_input)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)[0]

        if prediction == "spam":
            st.error("🚨 This message is **SPAM**!")
        else:
            st.success("✅ This message is **HAM** (Not Spam).")

