import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for i in distances[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Load the movies list and similarity matrix
movies_list = pickle.load(open("movie_dict.pkl", 'rb'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open("similarity.pkl", 'rb'))

# Streamlit user interface
st.title('Movie Recommendation System')

# Dropdown menu for movie selection
selected_movie_name = st.selectbox(
    "What would you like to watch?",
    movies['title'].values
)

st.write("You selected:", selected_movie_name)

# Button to generate recommendations
if st.button("Get Recommendations"):
    st.write("Here is a list of recommendations:")
    recommendations = recommend(selected_movie_name)
    for movie in recommendations:
        st.write(movie)
