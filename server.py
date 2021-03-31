from flask import Flask

app = Flask(__name__)
@app.route('/')

def home():
    return "oh thomas ur turning on my hot spot"

if __name__ == '__main__':
    app.run()