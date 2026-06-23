# SMS Spam Classifier
An **SMS Spam Classification System** built using **Machine Learning, Natural Language Processing (NLP), and Streamlit** that classifies incoming SMS messages as **Spam** or **Not Spam (Ham)** in real time.

## Live Demo

🔗 https://your-streamlit-app-url.streamlit.app/

---

## Features

- Detect whether an SMS is Spam or Not Spam
- Real-time message classification
- Text preprocessing using NLP techniques
- TF-IDF Vectorization
- Machine Learning-based prediction
- Interactive Streamlit web interface
- Responsive and user-friendly design

---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- NLTK
- Streamlit
- Pickle

---

## Dataset

The dataset contains:
- SMS Text Messages
- Spam Messages
- Ham (Non-Spam) Messages

### Example

| Message | Label |
|----------|----------|
| Congratulations! You have won ₹50,000. Claim now! | Spam |
| Hey, are we meeting tomorrow? | Ham |

---

## Project Workflow

### 1. Data Collection
Collected the SMS Spam Collection Dataset.

### 2. Data Cleanin
- Removed unnecessary columns
- Handled missing values
- Removed duplicate messages

### 3. Text Preprocessing
- Converted text to lowercase
- Tokenization
- Removed punctuation
- Removed stopwords
- Applied stemming using Porter Stemmer

### 4. Feature Engineerin
Transformed text into numerical features using:
- TF-IDF Vectorization

### 5. Model Training
Trained and evaluated multiple machine learning algorithms:

- Multinomial Naive Bayes
- Support Vector Machine (SVM)
- Random Forest
- Decision Tree
- Extra Trees Classifier

### 6. Model Evaluation
Performance was evaluated using:
- Accuracy Score
- Precision Score

### 7. Prediction System
The user enters an SMS message and the system predicts whether it is:
- Spam 🚨
- Not Spam ✅

### 8. Streamlit Web App Deployment
Deployed the application using Streamlit Community Cloud.

---

## Screenshots 📸

### Home Page

![Home Page](screenshots/home.png)

### Prediction Result

![Prediction Result](screenshots/result.png)

---

## Installation

### Clone Repository
```bash
git clone https://github.com/anjalikumari31-sudo/SMS-Spam-Classifier.git
```

### Move into Project Folder
```bash
cd SMS-Spam-Classifier
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Application
```bash
streamlit run app.py
```

---
## Project Structure

```text
SMS-Spam-Classifier/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── .gitignore
└── README.md
```

---


---

## Acknowledgement

This project was developed by following and learning from the **CampusX SMS Spam Classifier tutorial**. I implemented the machine learning pipeline, customized the Streamlit user interface, deployed the application using **Streamlit Community Cloud**, and made enhancements to improve usability and user experience.

---

## Author

**Anjali Kumari**

GitHub: https://github.com/anjalikumari31-sudo

