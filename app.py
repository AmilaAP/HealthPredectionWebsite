from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict')
def predict():
    return render_template('predict.html')


if __name__ == '__main__':
    app.run()