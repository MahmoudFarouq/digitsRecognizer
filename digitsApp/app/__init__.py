
from app.model import getModel

model = getModel()



from flask import Flask

app = Flask(__name__)
UPLOAD_FOLDER = '/home/sorcerer/Desktop/digitsApp/app/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from app import routes

