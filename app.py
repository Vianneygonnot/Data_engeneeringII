from flask import Flask, request, render_template
import time
import statistics
import pickle
import sklearn.linear_model
import sklearn.feature_extraction.text

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analysis', methods = ['POST'])
def analysis():
    text = request.form.get('phrase', "shitty")
    pred = model.predict_proba(vectorizer.transform([text]))

    '''return render_template("index.html",prediction_text = 'The sentence "{}" is neg {} pos {}'.format(text,pred[0][0],pred[0][1]))'''
    
    if pred[0][1] < 0.4:
        return render_template('negative.html')
    elif pred[0][1] > 0.4 and pred[0][1] < 0.6:
        return render_template('neutral.html')
    else :
        return render_template('positive.html')
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)