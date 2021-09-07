from textblob import TextBlob, Word
from flask import Flask, request
from flask.templating import render_template

#flask initilaization
app = Flask(__name__)

#Homepage 
@app.route('/')
def home_page():
    return render_template('home_page.html')


@app.route('/', methods = ['get', 'post'])
def result():
    input = request.form.get('paragraph')
    meaning = Word(input.lower()).spellcheck()
    return render_template('home_page.html', meaning = meaning, input = input)
if __name__ == '__main__':
    app.run(debug = True)
