import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        movie_id=i[0]
        #fetch poster from API
        recommended_movies.append(movies_df.iloc[i[0]].title)
    return recommended_movies

movies_df = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_df['title'].values
st.title('Movie Recommender System')
option = st.selectbox('Select a movie', movies_list)
st.write('You selected:', option)
similarity = pickle.load(open('similarity.pkl', 'rb'))

if st.button("Recommend", type="primary"):
    recommendations = recommend(option)
    for i in recommendations:
        st.write(i)
        
