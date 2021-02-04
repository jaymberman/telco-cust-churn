from flask import Flask, render_template, request, send_file
from flask import after_this_request
import pandas as pd
from numpy import float64
import tempfile
import os
import sklearn
from joblib import load

TEMPDIR = tempfile.mkdtemp()
PATH = os.path.join(TEMPDIR, 'churn_predictions.csv')
PREPROCESSOR = load('src/data_preprocessing_pipeline.joblib')
MODEL = load('src/model.joblib')


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/single_result', methods=['POST'])
def single_result():
    usr_input = [str(x) for x in request.form.values()]
    df = pd.DataFrame([usr_input])
    df.loc[:, 4] = df.loc[:, 4].astype(float64)
    df.loc[:, 17] = df.loc[:, 17].astype(float64)
    df.columns = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 'MultipleLines', 'InternetService',
                  'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
                  'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges']
    X = PREPROCESSOR.transform(df)
    proba = MODEL.predict_proba(X)
    print(MODEL.classes_)
    return render_template('home.html', 
                            text=f'Probability of Customer Leaving: {proba[0][1] * 100}%')


def _do_data_science(df):
    df += 10
    return df

@app.route('/success', methods=['POST'])
def fileupload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "file not in request.files"
        file = request.files['file']
        df = pd.read_csv(file, header=None)
        df = _do_data_science(df)
        df.to_csv(PATH)
        return render_template('file.html')
    else:
        return "not a POST request"

@app.route('/download')
def download():
    @after_this_request
    def remove_file(response):
        os.remove(PATH)
        return response

    return send_file(PATH, as_attachment=True)