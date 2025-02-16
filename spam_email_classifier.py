!pip install pandas scikit-learn nltk matplotlib flask streamlit joblib

from google.colab import files
uploaded = files.upload()  # Upload the dataset (e.g., sms_spam.csv)

import pandas as pd

# Load dataset
data = pd.read_csv("SMSSpamCollection.csv", encoding='latin-1', names=["label", "message"])
data = data[["label", "message"]]  # Remove unnecessary columns
print(data.head())

import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download NLTK stopwords
nltk.download('stopwords')

# Text preprocessing
ps = PorterStemmer()

def preprocess_text(text):
    words = [ps.stem(word) for word in text.lower().split() if word not in stopwords.words('english')]
    return ' '.join(words)

data['processed_message'] = data['message'].apply(preprocess_text)

# Encode labels
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# Split data
X = data['processed_message']
y = data['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert text to numeric features
cv = CountVectorizer(max_features=5000)
X_train_vec = cv.fit_transform(X_train).toarray()
X_test_vec = cv.transform(X_test).toarray()

# Train Naive Bayes Classifier
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Test and evaluate
y_pred = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

def predict_email(text):
    processed_text = preprocess_text(text)
    text_vec = cv.transform([processed_text]).toarray()
    prediction = model.predict(text_vec)
    return "Spam" if prediction[0] == 1 else "Not Spam"

# Example usage
email = "Congratulations! You've won a $1,000 gift card. Click here to claim now."
print(predict_email(email))

import matplotlib.pyplot as plt

data['label'].value_counts().plot(kind='bar', color=['blue', 'orange'])
plt.title('Spam vs Ham Distribution')
plt.xlabel('Label')
plt.ylabel('Count')
plt.show()

import joblib

# Save the model and vectorizer
joblib.dump(model, 'spam_classifier_model.pkl')
joblib.dump(cv, 'count_vectorizer.pkl')

# Download the model files
from google.colab import files
files.download('spam_classifier_model.pkl')
files.download('count_vectorizer.pkl')