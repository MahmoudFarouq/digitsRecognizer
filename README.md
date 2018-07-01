# digitsRecognizer
### flask web app for digits recognition
this app works by allowing the users to draw a digit from 0 to 9 and it predicts what the digit is

## dependencies
```shell
sudo pip3 -H install numpy sklearn matplotlib pillow flask mnist-python
```

## run
```shell
cd digitsApp
export FLASK_APP=main.py
flask run
```
and then go to localhost:5000/predict
