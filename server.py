from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from mtcnn.mtcnn import MTCNN
from matplotlib import pyplot
import warnings
from cv2 import imread
from PIL import Image, ImageDraw, ImageFilter
import os
import time



app = Flask(__name__)

imagePath = ''
def setPath(path):
    imagePath = path

EMOJI_FOLDER = os.path.join('static', 'res')

uploads_dir = os.path.join('static', 'uploads')
os.makedirs(uploads_dir, exist_ok=True)

IMAGE_FOLDER = os.path.join('static', 'results')

app.config['UPLOAD_FOLDER'] = uploads_dir
app.config['RES_FOLDER'] = EMOJI_FOLDER
app.config['RESULTS_FOLDER'] = IMAGE_FOLDER

emojiPath = os.path.join(app.config['RES_FOLDER'], 'emoji.png')
im2 = Image.open(emojiPath)

pixels = imread(imagePath)

detector = MTCNN()

@app.route('/')
def home():
    return render_template('SmileyNator.html')

@app.route('/getImage', methods=['POST'])
def saveImg():
    if request.method == 'POST':
        f = request.files['file']
        fileName = f.filename
        f.save(os.path.join(uploads_dir, secure_filename(f.filename)))
        
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], fileName)

        im1 = Image.open(full_filename)
        pixels = imread(full_filename)

        faces = detector.detect_faces(pixels)

        for result in faces:
            x, y, width, height = result['box']

            size = (width + 40), (height + 40)
            im2.thumbnail(size)
            im2.save(os.path.join(app.config['RES_FOLDER'], 'resize.png'), quality=100)
            im3 = Image.open(os.path.join(app.config['RES_FOLDER'], 'resize.png'))
            im1.paste(im3, (x-15, y-5), im3)

        im1.save(os.path.join(app.config['RESULTS_FOLDER'], 'result.png'), quality=100)


        result_path = os.path.join(app.config['RESULTS_FOLDER'], 'result.png')
        
        return render_template('SmileyNator.html', user_image = result_path)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response
        

if __name__ == '__main__':
    app.run()
