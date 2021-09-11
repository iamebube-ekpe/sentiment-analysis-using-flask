from flask import Flask, render_template, url_for, request, jsonify
from flask_restful import Api, reqparse
from flask_cors import CORS
import tweepy as twt
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
# import matplotlib.pyplot as plt
# plt.style.use('fivethirtyeight')


app = Flask(__name__)
api = Api(app)
CORS(app, resources=r'/api/*')

# Cleaning the text using a function
def cleanTxt(text):
    text =re.sub(r'@[A-Za-z0-9_]+', '', text) # Removing @mentions
    text = re.sub(r'#', '', text) # Removing Hashtags
    text = re.sub(r'RT[\s]+:', '', text) # Removing RT
    text = re.sub(r'https?:\/\/\S+', '', text) # Removing hyperlinks

    return text

# A function to get the subjectivity
def getSubject(text):
    return TextBlob(text).sentiment.subjectivity

# A funtion to get polarity
def getPolarity(text):
    return TextBlob(text).sentiment.polarity

# Create function to compute the negative, neutral and positive analysis
def getAnalysis(score):
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'

def analyzeSentiment(twtName, numTwts):
    logDets = pd.read_csv('Login.csv')

    # The Twitter API credentials
    consumerKey = logDets['key'][0]
    consumerSecret = logDets['key'][1]
    accessToken = logDets['key'][2]
    accessTokenSecret = logDets['key'][3]

    # Auth Object
    authenticate = twt.OAuthHandler(consumerKey, consumerSecret)

    # Set access token and access token secret
    authenticate.set_access_token(accessToken, accessTokenSecret)

    # Create API object
    api = twt.API(authenticate, wait_on_rate_limit=True)

    # Extract 100 tweets from Twitter user
    posts = api.user_timeline(id = twtName, count=numTwts, lang = 'en', tweet_mode = 'extended')

    # Create dataframe with column called tweets
    df = pd.DataFrame([tweet.full_text for tweet in posts], columns=['Tweets'])

    
    df['Tweets'] = df['Tweets'].apply(cleanTxt) # Cleaning the texts

    # Adding two new columns
    df['Subjectivity'] = df['Tweets'].apply(getSubject)
    df['Polarity'] = df['Tweets'].apply(getPolarity)

    df['Analysis'] = df['Polarity'].apply(getAnalysis)

    df_dict = df.to_dict(orient='list')

    return df_dict


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/api/analyze', methods=['POST'])
def sentiment():
    parser = reqparse.RequestParser()
    parser.add_argument('twtId',
        type=str,
        required=True,
        help="This field cannot be left blank!")
    parser.add_argument('numOfTwts',
        type=int,
        required=True,
        help="This field cannot be left blank!")

    if request.method == 'POST':
        args = parser.parse_args()
        twtId = args['twtId']
        numOfTwts = args['numOfTwts']
        twts = analyzeSentiment(twtId, numOfTwts)

        print(f'{twtId}, {numOfTwts}\n{twts}')

        return jsonify(twts)




if __name__ == '__main__':
    app.run(debug=True)