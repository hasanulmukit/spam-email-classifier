# Spam Email Classifier

This project is a **Spam Email Classifier** built using Python and Streamlit. It uses a pre-trained model to predict whether an email is **Spam** or **Not Spam**. The app also provides the probability scores for both categories, enhancing transparency and reliability of the prediction.

## Features

- **Interactive Interface**: A user-friendly Streamlit interface.
- **Text Input**: Allows users to input email text directly.
- **File Upload**: Accepts `.txt` files containing email content.
- **Detailed Results**:
  - Displays prediction as "Spam" or "Not Spam."
  - Shows probabilities for both categories.
- **Custom Styling**: Enhanced aesthetics with styled headers, buttons, and footers.

## Tech Stack

- **Programming Language**: Python
- **Framework**: Streamlit
- **Libraries**: Scikit-learn, Joblib

## Installation Guide

### Prerequisites

1. **Python**: Ensure Python (>=3.8) is installed.
   - [Download Python](https://www.python.org/downloads/)
2. **Streamlit**: Install using pip.
   ```bash
   pip install streamlit
   ```
3. **Joblib**: Ensure joblib is installed.
   ```bash
   pip install joblib
   ```

### Steps to Run

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/SpamEmailClassifierApp.git
   cd SpamEmailClassifierApp
   ```

2. **Add the Pre-trained Model**:

   - Save the trained model (`spam_classifier_model.pkl`) and vectorizer (`count_vectorizer.pkl`) in the project directory.

3. **Run the App**:

   ```bash
   streamlit run app.py
   ```

4. **Access the App**:

   - Open the URL displayed in the terminal (default: [http://localhost:8501/](http://localhost:8501/)).

## Usage

### Input Methods

1. **Direct Text Input**:
   - Paste email content into the provided text box.
2. **File Upload**:
   - Upload a `.txt` file containing the email content.

### Output

- **Prediction**:
  - Displays whether the email is "Spam" or "Not Spam."
- **Probabilities**:
  - Shows the likelihood of the email belonging to each category.

## Future Enhancements

- **Deployment**:
  - Deploy on platforms like Heroku or Streamlit Cloud.
- **Enhanced Visualization**:
  - Add graphical visualizations for probabilities.
- **Additional Input Formats**:
  - Support for PDF and DOCX file uploads.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Streamlit Documentation: [Streamlit](https://docs.streamlit.io/)
- Scikit-learn: [Scikit-learn](https://scikit-learn.org/)
