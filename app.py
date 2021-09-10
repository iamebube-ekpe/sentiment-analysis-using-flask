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

tweets = [ "qqwwwweerrttt", "ashhdskdjkksadjas", "asdsakdoiahdjfsfoijdas" ]

def analyzeSentiment(twtName, numTwts):
    pass

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

        print(f'{twtId}, {numOfTwts}')

    return jsonify({'message': 'success'})




if __name__ == '__main__':
    app.run(debug=True)