from flask import Flask
app = Flask('memeview')

@app.route('/')
def hello_world():
    return 'Hello, World!'
