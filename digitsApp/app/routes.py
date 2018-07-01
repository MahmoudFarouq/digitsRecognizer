import os

from flask import request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import base64

from app import app, model
from app.model import predictImage

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




@app.route('/', methods=['POST'])
def post_home():
    print(request.json)
    return 'donnne'

@app.route('/', methods=['POST'])
def get_home():
    return 'hiii from home'

@app.route('/predict', methods=['POST'])
def post_predict():
    import os
    s = request.json['image'] 
    imgdata = s + '='*(4-len(s)%4)
    imgdata = imgdata[imgdata.find(',')+1:]
    os.system("echo '{}' | base64 -d > image.jpg".format(imgdata))
    return str(predictImage(model, 'image.jpg')[0])
    

'''
file = None
    with open(request.form['image'], 'rb') as fp:
        file = FileStorage(fp)
    file.save('test_new.png')
'''

'''
@app.route('/predict', methods=['POST'])
def post_predict():
    # check if the post request has the file part
    if 'imageInput' not in request.files:
        return redirect(request.url)
    file = request.files['imageInput']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        prediction = predictImage(model, os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print(prediction)
        return 'hi'
'''



@app.route('/predict', methods=['GET'])
def get_predict():
    return render_template('predictingPage.html')


@app.route('/', methods=['GET'])
def index():
    return 'hiii'