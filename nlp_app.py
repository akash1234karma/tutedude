import streamlit as st
import pickle
import joblib
import nltk
import pandas as pd

st.title('Movie Recommendation System')
with open("movie.pickle",'rb') as m:
    movies=pickle.load(m)

similarity=joblib.load('similarities.joblib')

movie_name=movies['title'].values

def recommend(name_movies):
    movie_index=movies[movies['title']==name_movies].index[0]
    recommendations=similarity[movie_index]
    movie_list=sorted(enumerate(recommendations), reverse=True, key=lambda x:x[1])[1:6]
    recommend_movies=[]
    for i in movie_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies

name_movies=st.selectbox("Enter the movie", movie_name)
if st.button("Recommend"):
    r=recommend(name_movies)
    st.write("movies are:")
    for i in r:
        st.write(i)