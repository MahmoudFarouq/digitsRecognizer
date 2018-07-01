import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.linear_model import SGDClassifier
from sklearn.neural_network import MLPClassifier

from PIL import Image

from mnist import MNIST

import os
import pickle


def createModel():
    pathToDataDir = 'dataset'
    mndata = MNIST(pathToDataDir)

    X_train, y_train = mndata.load_training()
    X_train, y_train = np.array(X_train), np.array(y_train)
    X_test , y_test  = mndata.load_testing()
    X_test , y_test  = np.array(X_test), np.array(y_test)


    # clf = SGDClassifier(loss='log', alpha=0.001, max_iter=512, n_jobs=-1)
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(1024, 512), random_state=1)
    clf.fit(X=X_train, y=y_train)
    print("model accuracy is: %s"%accuracy_score(y_test, clf.predict(X_test)))

    return clf


def getModel(model_file = 'model.pkl'):
    if model_file in os.listdir():
        model = pickle.load(open(model_file,"rb"))
    else:
        model = createModel()
        pickle.dump(model, open(model_file,"wb"))
    return model


def predictImage(model, path):
    img = Image.open(path).convert('LA')
    img = img.resize((28,28))
    img = np.array(img)[:,:,0].reshape(1, -1)
    return model.predict(img)


def Test():
    data = load_digits()
    X, y = data.data, data.target.reshape(-1, 1)
    model = getModel()
    path = '/home/sorcerer/Desktop/digitsApp/app/images/'
    images = sorted(os.listdir(path))
    for i in range(10):
        imgP = path + images[i]
        print(predictImage(model, imgP) , y[i])


def createImages():
    from matplotlib.image import imsave
    data = load_digits()
    X, y = data.data, data.target.reshape(-1, 1)
    path = '/home/sorcerer/Desktop/digitsApp/app/images/'
    for i in range(10):
        imsave(path+'%05.f.png'%(i+1), X[i, :].reshape(28,28), cmap='gray')
