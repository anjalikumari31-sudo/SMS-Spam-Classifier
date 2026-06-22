import streamlit as st
import pickle
import nltk
nltk.download('punkt_tab')
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()
import string


tfidf=pickle.load(open('vectorizer.pkl', 'rb'))
model=pickle.load(open('model.pkl','rb'))

st.title('SMS Spam Classifier')
st.markdown("""
<style>

label[data-testid="stWidgetLabel"] p{
    font-size:22px !important;
    font-weight:bold;
    color:white;
}
.stApp{
    #background: linear-gradient(135deg,#0f172a,#1e293b);
    
}

.main-container{
    background-color: rgba(255,255,255,0.08);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0px 0px 20px rgba(0,0,0,0.4);
}

.title{
    text-align:center;
    color:white;
    font-size:50px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:#cbd5e1;
    margin-bottom:30px;
}

.stButton>button{
    width:100%;
    background:lavender;
    color:black;
    border-radius:20px;
    height:80px;
    font-size:40px;
    font-weight:bold;
}
.stButton>button:hover{
    background:#1d4ed8;
}


</style>
""", unsafe_allow_html=True)


def transform_text(SMS):
  text= SMS.lower() # lower case
  text=nltk.word_tokenize(text) # tokenization

  y=[]
  for i in text:
    if i.isalnum(): # allow only alpha numeric , not special characters
       y.append(i)

  text=y[:]
  y.clear()

  for i in text:
    if i not in stopwords.words('english') and i not in string.punctuation: #remove stopwords and punctuation
      y.append(i)

  text=y[:]
  y.clear()

  for i in text:
    y.append(ps.stem(i))  # stemming
  return " ".join(y)

#input_sms=st.text_area('Enter your message')
input_sms = st.text_area(
    "✉️ Enter your message",
    height=150,
    placeholder="Type your SMS here..."
)
if st.button('Predict'):

  # 1.preprocess
  transformed_sms = transform_text(input_sms)
  # 2.vectorize
  vector_input = tfidf.transform([transformed_sms])
  # 3.predict
  result = model.predict(vector_input)[0]
  # 4.display
  if result == 1:
    st.header('Spam')
  else:
    st.header(' Not Spam')



