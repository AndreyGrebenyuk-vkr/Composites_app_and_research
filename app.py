from flask import Flask, render_template, request, jsonify
import numpy as np
from static.src.predictor import final_props_predictor, ratio_predictor

app = Flask(__name__)

@app.route('/')
def final_props():
    return render_template('final_props.html')

@app.route('/predict/final_props', methods = ['POST'])
def get_predicted_props():
    data = request.form
    input_features = np.array([
        float(data['matrix_filler_ratio']),
        float(data['density']),
        float(data['elasticity_modulus']),
        float(data['hardener_amount']),
        float(data['epoxy_groups_amount']),
        float(data['flash_point']),
        float(data['surface_density']),
        float(data['resin_consumption']),
        float(data['patch_angle']),
        float(data['patch_pitch']),
        float(data['patch_density'])
    ]).reshape(1,-1)

    model = final_props_predictor()
    predictions = model.get_prediction(input_features)

    response = jsonify({
        'tensile_modulus_of_elasticity':predictions[0],
        'tensile_strength': predictions[1]
    })

    return response, 200, {'Content-Type': 'application/json'}

@app.route('/mf_ratio')
def mf_ratio():
    return render_template('matrix_filler_ratio.html')

@app.route('/predict/ratio', methods = ['POST'])
def get_predicted_ratio():
    data = request.form
    input_features = np.array([
        float(data['tensile_modulus_of_elasticity']),
        float(data['tensile_strength']),
    ]).reshape(1,-1)

    model = ratio_predictor()
    prediction = model.get_prediction(input_features)

    response = jsonify({
        'matrix_filler_ratio': prediction[0]
    })

    return response, 200, {'Content-Type': 'application/json'}

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)