import streamlit as st
import pickle as pkl
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()
def func(text):
    text=text.lower()
    text=nltk.word_tokenize(text)
    # return text
    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)
    text=y[:]
    y.clear()
    for i in text:
        if ((i not in (stopwords.words('english'))) and (i not in (string.punctuation))):
            y.append(ps.stem(i))
    return " ".join(y)
model=pkl.load(open('model.pkl','rb'))
vectorizer=pkl.load(open('vectorizer.pkl','rb'))
st.title('Spam Classifier')
ip=st.text_area('Enter the message')
if st.button('Predict'):
    text=func(ip)
    op=model.predict(vectorizer.transform([text]))[0]
    if op==1:
        st.header('Spam')
    else:
        st.header('Not Spam')