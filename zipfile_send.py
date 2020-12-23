from flask import Flask, render_template, request, send_file
from io import BytesIO
import zipfile

app = Flask(__name__)

@app.route("/getcaps",methods=['GET','POST'])
def downloadFiles():
    print(1)
    memory_file = BytesIO()
    print(2)
    print(send_file)
    with zipfile.ZipFile(memory_file, 'w') as zf:
        files = request.files
        for individualFile in files:
            data = zipfile.ZipInfo(individualFile['fileName'])
            data.date_time = time.localtime(time.time())[:6]
            data.compress_type = zipfile.ZIP_DEFLATED
            zf.writestr(data, individualFile['fileData'])
    memory_file.seek(0)
    return send_file(memory_file, attachment_filename='capsule.zip', as_attachment=True)

## おまじない
if __name__ == "__main__":
    app.run(debug=True,port=3000)