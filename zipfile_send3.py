from flask import Flask
import os, zipfile

app = Flask(__name__)

@app.route('/zip')
def downloadFiles():
    with zipfile.ZipFile('inu.zip','w') as myzip:
        for folder, subfolders, files in os.walk('dog'):
            myzip.write(folder)
            for file in files:
                myzip.write(os.path.join(folder,file))

## おまじない
if __name__ == "__main__":
    app.run(debug=True,port=3000)