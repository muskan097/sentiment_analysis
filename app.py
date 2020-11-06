from flask import Flask, request, render_template
import pickle
from flask_cors import cross_origin
import requests



app = Flask(__name__)
filename="sentiment.pkl"
classifier = pickle.load(open("sentiment.pkl", "rb"))
cv = pickle.load(open('cv-transform.pkl',"rb"))



@app.route('/')
@cross_origin()
def home():
    return render_template('home.html')

@app.route("/predict", methods= ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        message = request.form['message']
        data = [message]
        vect = cv.transform(data).toarray()
        my_prediction = classifier.predict(vect)
        return render_template('result.html', prediction=my_prediction)
     


if __name__ == '__main__':
    app.run(debug=True)
