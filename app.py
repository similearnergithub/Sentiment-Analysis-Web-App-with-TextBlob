from flask import Flask, request, render_template
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        text = request.form['text']
        blob = TextBlob(text)
        sentiment = blob.sentiment
        polarity = sentiment.polarity

        if polarity > 0:
            sentiment_result = "Positive"
        elif polarity < 0:
            sentiment_result = "Negative"
        else:
            sentiment_result = "Neutral"

        return render_template('index.html', text=text, sentiment_result=sentiment_result, polarity=polarity)

if __name__ == '__main__':
    app.run(debug=True)
