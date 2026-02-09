import streamlit as st
import json

base="light"
primaryColor="forestGreen"

# ==============================================================================
# Importing Required Data
# ==============================================================================

with open('./App/data/podcast_names.json', 'r') as f:
    podcast_names = json.load(f)

with open('./data/genres.json', 'r') as f:
    genres_list = json.load(f)

with open('./data/days.json', 'r') as f:
    days = json.load(f)

with open('./data/publication_time.json', 'r') as f:
    time = json.load(f)


podcasts_map = {"Athlete's Arena": 46.723734650096695,
 'Brain Boost': 44.502374696903615,
 'Business Briefs': 47.1126725807403,
 'Business Insights': 44.200050789037604,
 'Comedy Corner': 44.01677780841343,
 'Crime Chronicles': 47.730286299942094,
 'Criminal Minds': 43.59860028555392,
 'Current Affairs': 43.53176316592438,
 'Daily Digest': 45.71123949943967,
 'Detective Diaries': 46.56999211685686,
 'Digital Digest': 44.894253550405566,
 'Educational Nuggets': 45.83290442009784,
 'Fashion Forward': 45.32969686896353,
 'Finance Focus': 43.2573432753232,
 'Fitness First': 45.81604068013641,
 'Funny Folks': 45.12644830757489,
 'Gadget Geek': 47.099616068476976,
 'Game Day': 43.97879716314356,
 'Global News': 45.399679196900635,
 'Health Hour': 45.30267410724407,
 'Healthy Living': 45.209574386163005,
 'Home & Living': 46.312802051194254,
 'Humor Hub': 45.85645861477878,
 'Innovators': 45.9535998601466,
 'Joke Junction': 42.63949432930387,
 'Laugh Line': 44.468066701459605,
 'Learning Lab': 45.46308937970307,
 'Life Lessons': 45.181807014758874,
 'Lifestyle Lounge': 45.53314619754197,
 'Market Masters': 46.20585023679939,
 'Melody Mix': 48.13329069930533,
 'Mind & Body': 46.66583613892194,
 'Money Matters': 47.955538832287665,
 'Music Matters': 45.945354077870874,
 'Mystery Matters': 45.93303612797758,
 'News Roundup': 42.65358464826839,
 'Sound Waves': 44.42823407477307,
 'Sport Spot': 44.697550374894696,
 'Sports Central': 41.74285059612863,
 'Sports Weekly': 46.96406299036968,
 'Study Sessions': 46.834017419818096,
 'Style Guide': 45.009454883735955,
 'Tech Talks': 46.270802759759924,
 'Tech Trends': 44.59238142207126,
 'True Crime Stories': 46.20019379874599,
 'Tune Time': 46.9193279239406,
 'Wellness Wave': 45.94061818584811,
 'World Watch': 44.00374133464532}


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
    
        genre = st.selectbox(
            "Select the genre of the episode:",
            options= genres_list
        )

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

st.divider()

import backend
    
st.markdown("""<style>
            .st-emotion-cache-13gev4o{
                align_self: center;
            }
            .st-emotion-cache-3pwa5w{
                text-align: center;
                }
            .st-emotion-cache-p75nl5{
                margin: auto;
            }

            .st-emotion-cache-1bwe20w{
                font-size: 1.2rem !important;
            }
            </style> """, unsafe_allow_html=True)

if st.button('Predict', key='predict_button', type='primary', use_container_width=True):

    with st.empty():
        st.markdown("""
                    <style>
                        .st-emotion-cache-1bwe20w{font-size: 1.3rem !important;}
                    </style>""", unsafe_allow_html=True)
        st.image('https://i.imgur.com/496a9Yz.gif', caption='Predicting...')

        prediction = backend.predict(lenght, host_popularity, guest_popularity, missing_guest, podcast, title, genre, ads, sentiment, publication_day, publication_time)
        st.write('')
    
    st.markdown(
        f"""
        <div style="
            display:flex; 
            align-items:center; 
            background-color:#18162F; 
            border:1px solid #118DFF; 
            border-radius:8px; 
            padding:15px;
            max-width:400px;
            margin: auto;
            overflow: ">
                    
        <div style="display:flex; flex-direction:column; text-align: left;">
            <span style="font-size:22px; font-weight:bold;">Average listening time for this episode:</span>
            <span style="font-size:46px; color:#118DFF;">{prediction} min</span>
            </div>
        
        <img src="https://i.imgur.com/SmKs4JV.png" width="100px" style="margin-right:10px;">
            
        </div>
        """,
        unsafe_allow_html=True)