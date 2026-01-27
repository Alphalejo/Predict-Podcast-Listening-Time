import streamlit as st
import json
import joblib

# ==============================================================================
# Importing Required Data
# ==============================================================================

with open('./data/podcast_names.json', 'r') as f:
    podcast_names = json.load(f)

with open('./data/genres.json', 'r') as f:
    genres_list = json.load(f)

with open('./data/days.json', 'r') as f:
    days = json.load(f)

with open('./data/publication_time.json', 'r') as f:
    time = json.load(f)


podcasts_map = joblib.load('../artifacts/podcast_target_encoding.pkl').to_dict()


# ==============================================================================
# UI
# ==============================================================================

# header
st. markdown("""
<h1 style='text-align: center;'>Predict the Listening Time of Your Podcast Episode</h1>""",
unsafe_allow_html=True)

st.divider()

st.markdown(""" 
    <style>        
        .st-key-advanced_toggle{
            transform: scale(1.5);
            align-self: center;
            padding-left: 5px;}
        
        .st-emotion-cache-gi0tri{
            display: none;}
    </style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([4,1,4])

with col1:
    st.markdown('<h4 style="text-align: right;">Quick Prediction</h4>', unsafe_allow_html=True)

with col2:
    advanced_predictions = st.toggle('', key='advanced_toggle')

with col3:
    st.markdown('<h4 style="text-align: left;">Advance Prediction</h4>', unsafe_allow_html=True)

# ----------------------------------------------------------
#  Quick Prediction
st.divider()

col1, col2 = st.columns([2, 3])
with col1:
    lenght = st.number_input('Episode Length (in minutes):', min_value= 1, max_value= 300, value= 65, step= 1)
    st.write('')
    st.write('')
    guest = st.toggle('Will a Guest be present?')

with col2:
    host_popularity = st.slider('Host Popularity (%):', min_value= 0, max_value= 100, value= 60, step= 1)
    if guest:
        guest_popularity = st.slider('Guest Popularity (%)', min_value=0, max_value=100, step=1, value=52)
        missing_guest = 0
    else:
        guest_popularity = 52.51  # Average Popularity when no guest is present
        missing_guest = 1
# ----------------------------------------------------------
# Advanced Prediction

if advanced_predictions:

    st.divider()
    st.write('Advanced Options')

    name_col, episode_col = st.columns([3,2])

    with name_col:
        podcast_raw = st.selectbox(
            "Select the podcast to analyze:",
            options=podcast_names
        )
        podcast = podcasts_map[podcast_raw]
    
        genre_raw = st.selectbox(
            "Select the genre of the episode:",
            options= genres_list
        )
        genre = genres_list[genre_raw]

    with episode_col:
        title = st.number_input('Episode Number:', min_value= 1, max_value= 300, value= 1, step= 1)

        ads = st.number_input('Number of Ads in the Episode (0-10):', min_value=0, max_value=10, value=1, step=1)


    col1, col2, col3 = st.columns(3)

    with col1:
        sentiment = st.selectbox('Episode Sentiment:', options=['Positive', 'Neutral', 'Positive'])

    with col2:
        raw_day = st.selectbox('Day to Publish', options=days)
        publication_day = days[raw_day]

    with col3:
        raw_time = st.selectbox('Time to Publish', options=time)
        publication_time = time[raw_time]

else:
    podcast = 46.723734650096695
    title = 1
    genre = 'News'
    ads = 1
    sentiment = 'Neutral'
    publication_day = 2
    publication_time = 12


    