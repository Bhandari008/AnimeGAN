from flask import Flask, request, render_template, redirect, url_for
from utils import translate_image
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        model_name = request.form["items"]
        filename = file.filename
        filepath = os.path.join('static/images/original', filename)
        file.save(filepath)
        translated_image = translate_image(filepath, model_name)
        return render_template('display_image.html',image =translated_image, model_name = model_name)
    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)