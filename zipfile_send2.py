from flask import Flask, render_template, request, send_file
from io import BytesIO
import zipfile

app = Flask(__name__)

@app.route('/')
def downloadFiles():
    with zipfile.ZipFile('hello.zip', "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write("cat1.jpg", "cat1.jpg") 

## おまじない
if __name__ == "__main__":
    app.run(debug=True,port=5000)