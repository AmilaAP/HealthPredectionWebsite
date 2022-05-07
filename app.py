import pandas as pd
import pickle
import flask
from flask import Flask
from flask import render_template

app = Flask(__name__)


def get_model():
    with open('model/model.pkl', 'rb') as file:
        model = pickle.load(file)

    print('success')
    return model


def get_form_data():
    if flask.request.method == 'POST':
        inputs = pd.DataFrame(
            columns=[])
        inputs = inputs.append(flask.request.form.to_dict(), ignore_index=True)
        inputs = inputs.astype(float)

    print('success')
    return inputs


def make_prediction():
    model = get_model()
    inputs = get_form_data()
    predictions = model.predict(inputs)

    print('success')
    return predictions


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict')
def predict():
    pred = make_prediction()
    return render_template('predict.html', preds=pred)


@app.route('/result')
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run()
