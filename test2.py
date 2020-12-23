from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello')
def hello():
    name = "Hello World"
    return name

@app.route('/good')
def good():
    name = "Good"
    return name

@app.route('/aaa')
def aaa():
    html = render_template('test.html')
    return html

## おまじない
if __name__ == "__main__":
    app.run(debug=True,port=5000)