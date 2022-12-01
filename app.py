from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world, welcome to my nori0227.tech page!'


## Note, if you want to run this app with the command `python app.py`, you need to add the following line to the end of the file
## so it can execute and stay running....
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

