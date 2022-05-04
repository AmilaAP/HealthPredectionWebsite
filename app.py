from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict')
def predict():
    return render_template('predict.html')


@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/predictnew')
def predictnew():
    return render_template('predictnew.html')


if __name__ == '__main__':
    app.run()