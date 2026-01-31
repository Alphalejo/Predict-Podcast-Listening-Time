import numpy as np
import pandas as pd
import joblib

def predict(
lenght = 65,
host_popularity = 60,
guest_popularity = 52.51,  # Average Popularity when no guest is present
missing_guest = 1,
podcast = 46.723734650096695,
title = 1,
genre = 'News',
ads = 1,
sentiment_raw = 'Neutral',
publication_day = 2,
publication_time = 12):

    sentiment_map = {
        'Negative': -1,
        'Neutral': 0,
        'Positive': 1
    }

    sentiment = sentiment_map[sentiment_raw]

    genre_map = {
        'Business': 45.55244226723161,
        'Comedy': 44.48775637598833,
        'Education': 45.69957544537044, 
        'Health': 45.81918055381969, 
        'Lifestyle': 45.4409049194452, 
        'Music': 46.533255061929985, 
        'News': 44.37182458341537, 
        'Sports': 44.913403840628156, 
        'Technology': 45.72374847377965, 
        'True Crime': 45.99179846445972 
    }

    # Encoding for  hours (0-23)
    Time_sin = np.sin(2 * np.pi * publication_time / 24)
    Time_cos = np.cos(2 * np.pi * publication_time / 24)

    # encoding for days (0-6)
    Day_sin = np.sin(2 * np.pi * publication_day / 7)
    Day_cos = np.cos(2 * np.pi * publication_day / 7)

    model = joblib.load('../Models/random_forest_model_encoded.pkl')
    
    data = {'Episode_Title': title,
            'Episode_Length_minutes': lenght,
            'Host_Popularity_percentage': host_popularity,
            'Guest_Popularity_percentage': guest_popularity,
            'Number_of_Ads': ads,
            'Episode_Sentiment': sentiment,
            'Guest_Popularity_missing': missing_guest,
            'Genre_encoded': genre_map[genre],
            'Time_sin': Time_sin,
            'Time_cos': Time_cos,
            'Day_sin': Day_sin,
            'Day_cos': Day_cos,
            'Podcast_Encoded': podcast}
    
    input_data = pd.DataFrame([data])

    prediction = model.predict(input_data)

    return prediction[0].round(2)