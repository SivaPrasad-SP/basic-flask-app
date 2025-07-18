from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1 style='text-align: center; margin-top: 100px;'>Hello, Flask project is working..!</h1>"

@app.route("/other")
def other():
    return "<h1 style='text-align: center; margin-top: 100px;'> ----- This is another route ----- </h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', post=5000)
