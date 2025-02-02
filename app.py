import streamlit as st
import joblib

# Load the saved model and vectorizer
model = joblib.load('spam_classifier_model.pkl')
vectorizer = joblib.load('count_vectorizer.pkl')

# Streamlit app interface
st.set_page_config(page_title="Spam Email Classifier", page_icon="📧", layout="centered")

# Title and styling
st.title("Spam Email Classifier")
st.markdown(
    """<style>
        .stTitle { color: #2E86C1; font-size: 36px; font-weight: bold; }
        .stButton button { background-color: #28A745; color: white; font-size: 16px; }
    </style>""",
    unsafe_allow_html=True
)
st.subheader("Predict whether an email is Spam or Not Spam")

# File upload
uploaded_file = st.file_uploader("Upload a .txt file with email content:", type="txt")
email_text = ""
if uploaded_file is not None:
    email_text = uploaded_file.read().decode("utf-8")
    st.text_area("Email Content", email_text, height=200)

# Input text area
if not uploaded_file:
    email_text = st.text_area("Or enter the email text below:", height=200)

# Prediction button
if st.button("Classify"):
    if email_text.strip() == "":
        st.error("Please provide email content for classification.")
    else:
        # Preprocess and predict
        email_vectorized = vectorizer.transform([email_text]).toarray()
        prediction = model.predict(email_vectorized)[0]
        probabilities = model.predict_proba(email_vectorized)[0]

        result = "Spam" if prediction == 1 else "Not Spam"
        spam_prob = round(probabilities[1] * 100, 2)
        not_spam_prob = round(probabilities[0] * 100, 2)

        # Display results
        st.success(f"Prediction: {result}")
        st.markdown(
            f"""### Probabilities:
            - **Spam:** {spam_prob}%
            - **Not Spam:** {not_spam_prob}%
            """
        )

# Add footer
st.markdown("""<style>
.footer { font-size: 14px; color: gray; text-align: center; margin-top: 50px; }
</style>
<div class="footer">
Built with ❤️ by Hasanul Mukit
</div>""", unsafe_allow_html=True)