
import joblib
import tensorflow as tf
from catboost import CatBoostRegressor

class final_props_predictor:
    def __init__(self):
        self.model = tf.keras.models.load_model('static/models/nn_stregth_elasticity.keras')
        with open('static/models/scalers.save', 'rb') as f:
            self.features_scaler, self.targets_scaler = joblib.load(f)

    def get_prediction(self, _inputs):
        inputs = self.features_scaler.transform(_inputs)
        predictions = self.model.predict(inputs)
        predictions = self.targets_scaler.inverse_transform(predictions)
        return predictions
    
class ratio_predictor:
    def __init__(self):
        self.model_nn = tf.keras.models.load_model('')
        self.model_cat = CatBoostRegressor().load_model('static/models/cat_mf.bin')
        with open('static/models/matrix_filler_features_scaler.save','rb') as f:
            self.features_scaler = joblib.load(f)
    
    def get_prediction(self, _inputs):
        inputs = self.features_scaler.transform(_inputs)
        prediction = self.model_cat.predict(self.model.predict(inputs))
        return prediction
