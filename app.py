from flask import Flask
from flask import render_template
app = Flask(__name__)

# change model file location for your model location
with open(f'model/sk_linear_model.pkl', 'rb') as file:
    model = pickle.load(file)

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
    return render_template('predict.html')


@app.route('/result')
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run()
