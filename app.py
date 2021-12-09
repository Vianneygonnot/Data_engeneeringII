from flask import Flask, request, render_template
import time
import statistics

app = Flask(__name__)

'''
@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST', 'GET'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
'''

@app.route('/', methods=['GET', 'POST'])
def my_form():
    if request.method == 'POST':
        text = request.form
    return render_template('my-form.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)