from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

def square(n):
    return n * n

@app.route('/square/<int:n>')
def square_route(n):
    result = square(n)
    return f"Square of {n} is {result+1}"

if __name__ == '__main__':
    app.run(debug=True)
