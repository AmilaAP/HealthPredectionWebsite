import pandas as pd
import pickle
import flask
import sklearn
from flask import Flask
from flask import render_template

app = Flask(__name__)

with open(f'model/model.pkl', 'rb') as file:
    model = pickle.load(file)


def get_model():
    with open('model/model.pkl', 'rb') as file:
        model = pickle.load(file)

    print('success')
    return model


def get_form_data():
    if flask.request.method == 'POST':
        inputs = pd.DataFrame(
            columns=['itching', 'skin_rash', 'continuous_sneezing', 'shivering', 'stomach_pain', 'acidity', 'vomiting',
                     'indigestion', 'muscle_wasting', 'patches_in_throat', 'fatigue', 'weight_loss', 'sunken_eyes',
                     'cough', 'headache', 'chest_pain', 'back_pain', 'weakness_in_limbs', 'chills', 'joint_pain',
                     'yellowish_skin', 'constipation', 'pain_during_bowel_movements', 'breathlessness', 'cramps',
                     'weight_gain', 'mood_swings', 'neck_pain', 'muscle_weakness', 'stiff_neck', 'pus_filled_pimples',
                     'burning_micturition', 'bladder_discomfort', 'high_fever', 'nodal_skin_eruptions',
                     'ulcers_on_tongue', 'loss_of_appetite', 'restlessness', 'dehydration', 'dizziness',
                     'weakness_of_one_body_side', 'lethargy', 'nausea', 'abdominal_pain', 'pain_in_anal_region',
                     'sweating', 'bruising', 'cold_hands_and_feets', 'anxiety', 'knee_pain', 'swelling_joints',
                     'blackheads', 'foul_smell_of urine', 'skin_peeling', 'blister', 'dischromic _patches',
                     'watering_from_eyes', 'extra_marital_contacts', 'diarrhoea', 'loss_of_balance',
                     'blurred_and_distorted_vision', 'altered_sensorium', 'dark_urine', 'swelling_of_stomach',
                     'bloody_stool', 'obesity', 'hip_joint_pain', 'movement_stiffness', 'spinning_movements',
                     'scurring', 'continuous_feel_of_urine', 'silver_like_dusting', 'red_sore_around_nose', 'missing',
                     'spotting_ urination', 'passage_of_gases', 'irregular_sugar_level', 'family_history',
                     'lack_of_concentration', 'excessive_hunger', 'yellowing_of_eyes', 'distention_of_abdomen',
                     'irritation_in_anus', 'swollen_legs', 'painful_walking', 'small_dents_in_nails',
                     'yellow_crust_ooze', 'internal_itching', 'mucoid_sputum', 'history_of_alcohol_consumption',
                     'swollen_blood_vessels', 'unsteadiness', 'inflammatory_nails', 'depression', 'fluid_overload',
                     'swelled_lymph_nodes', 'malaise', 'prominent_veins_on_calf', 'puffy_face_and_eyes',
                     'fast_heart_rate', 'irritability', 'muscle_pain', 'mild_fever', 'yellow_urine', 'phlegm',
                     'enlarged_thyroid', 'increased_appetite', 'visual_disturbances', 'brittle_nails',
                     'drying_and_tingling_lips', 'polyuria', 'pain_behind_the_eyes', 'toxic_look_(typhos)',
                     'throat_irritation', 'swollen_extremeties', 'slurred_speech', 'red_spots_over_body', 'belly_pain',
                     'receiving_blood_transfusion', 'acute_liver_failure', 'redness_of_eyes', 'rusty_sputum',
                     'abnormal_menstruation', 'receiving_unsterile_injections', 'coma', 'sinus_pressure',
                     'palpitations', 'stomach_bleeding', 'runny_nose', 'congestion', 'blood_in_sputum',
                     'loss_of_smell'])
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


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if flask.request.method == 'GET':
        print(flask.request.method)

        return render_template('predict.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    if flask.request.method == 'POST':
        data = flask.request.form.to_dict()

        print(f'{data}')

        return render_template('result.html', symptoms=data)


if __name__ == '__main__':
    app.run()
