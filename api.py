from flask import Flask, jsonify,request, render_template
from keras.models import load_model
import joblib


app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/api/modelo",methods=['POST'])
def modelo():
    data=request.get_json()
    Volumen= data['Volumen']
    Hour= data['Hour']
    Day= data['Day']
    Month= data['Month']
    Year= data['Year']

    scaler_path = "D:/modelo/scaler.pkl"
    scaler = joblib.load(scaler_path)

    X = scaler.transform([[Volumen, Hour, Day, Month, Year]])

    model_path = "D:/modelo/modelo.h5"
    ann = load_model(model_path)
    Prediccion = ann.predict(X)[0][0]

    error_absoluto=joblib.load("D:/modelo/errorAbsoluto.pkl")
    return jsonify(
        impresion=str(Prediccion),
        error_medio_absoluto= str(error_absoluto)
    )
if __name__ == "__main__":
    app.run()   