import os

from flask import Flask, render_template, request, flash, url_for, send_from_directory
from werkzeug.utils import redirect, secure_filename
from flask import jsonify
import pandas as pd
import pandasOperations
import json

app = Flask(__name__)
app.config['STORAGE_FOLDER'] = 'uploaded_file'
ALLOWED_EXTENSIONS = set(['xlsx', 'csv'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# api to upload file
@app.route('/try', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'data' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['data']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['STORAGE_FOLDER'], filename))
            pandasOperations.pandas_operations(os.path.join(app.config['STORAGE_FOLDER'], filename))
            return "Uploaded " + filename
        else:
            flash('File in wrong format.')
            return redirect(request.url)
    return render_template('upload.html')


# api for q1 output
@app.route('/q1/PC', methods=['GET'])
def q1_pc():
    pc = pd.read_csv('PC.csv')
    pc_json = pc.to_json(orient='records')
    return jsonify(pc_json)


# api for q1 output
@app.route('/q1/LPC', methods=['GET'])
def q1_lpc():
    lpc = pd.read_csv('LPC.csv')
    lpc_json = lpc.to_json(orient='records')
    return jsonify(lpc_json)


# api for q1 output
@app.route('/q1/plasmalogen', methods=['GET'])
def q1_plasmalogen():
    plasmalogen = pd.read_csv('PC.csv')
    plasmalogen_json = plasmalogen.to_json(orient='records')
    return jsonify(plasmalogen_json)


# api for q2 output
@app.route('/q2/data_new', methods=['GET'])
def q1_data():
    data_new = pd.read_csv('data_new.csv')
    data_new_json = data_new.to_json(orient='records')
    return jsonify(data_new_json)


# api for q3 output
@app.route('/q3/sample_means', methods=['GET'])
def q1_sample_means():
    sample_means = pd.read_csv('sample_means.csv')
    sample_means_json = sample_means.to_json(orient='records')
    return jsonify(sample_means_json)


if __name__ == "__main__":
    app.debug = True
    app.secret_key = '#SecretKey'
    app.run()
