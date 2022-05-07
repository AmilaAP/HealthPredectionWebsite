import pandas as pd
import pickle
import flask
from flask import Flask
from flask import render_template

app = Flask(__name__)

# change model file location for your model location
with open(f'model/sk_linear_model.pkl', 'rb') as file:
    model = pickle.load(file)

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

# check route to match your result page location
@app.route('/result', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return flask.render_template('index.html')

    if flask.request.method == 'POST':
        # change column values to your symptoms
        inputs = pd.DataFrame(
            columns=['LotFrontage', 'MasVnrArea', 'TotalBsmtSF', 'firstFlrSF', 'GrLivArea', 'FullBath',
                     'TotRmsAbvGrd', 'Fireplaces', 'GarageCars', 'GarageArea', 'MasVnrType', 'OverallQual',
                     'ExterQual', 'BsmtQual', 'HeatingQC', 'KitchenQual', 'FireplaceQu', 'YearBuilt',
                     'YearRemodAdd', 'GarageYrBlt', 'Age'])
        inputs = inputs.append(flask.request.form.to_dict(), ignore_index=True)
        inputs = inputs.astype(float)
        result = model.predict(inputs)

        # check return location
        return flask.render_template('result.html', result=result[0], )


@app.route('/predict')
def predict():
    pred = make_prediction()
    return render_template('predict.html', preds=pred)


@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/predictnew')
def predictnew():
    return render_template('predictnew.html')


if __name__ == '__main__':
    app.run()
