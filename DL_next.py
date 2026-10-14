import streamlit as st
import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences

model = tf.keras.models.load_model('nextword_model.keras')
with open('tokenizer.pkl','rb') as file:
    tokenizer=pickle.load(file)

reverse_index={idx:word for word, idx in tokenizer.word_index_items()}

max_len=44

def generate_text(seed_text,num_words=10):
    text=seed_text

    for _ in range(num_words):
        seq=tokenizer.texts_to_sequences([text])[0]
        padded=pad_sequences([seq],max_len,padding='pre')
        preds=model.predict(padded,verbose=0)
        pos=np.argmax(preds)
        next_word=reverse_index.get(pos,'')
        text += " "+ next_word
    return text

st.title("next word")
seed=st.text_input("enter text",'Hello')
num_words=st.slider('num of word generate', 1,20,10)

if st.button('Generate'):
    result=generate_text(seed, num_words)
    st.write(result)