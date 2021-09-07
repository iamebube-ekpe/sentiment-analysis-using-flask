from flask import Flask, render_template, url_for
from flask_restful import Api, reqparse
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')





if __name__ == '__main__':
    app.run(debug=True)