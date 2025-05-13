from flask import Flask, render_template, request
import os 

app = Flask(__name__)
app.config['UPLOAD_FOLDER']  = "dfd"
    
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/upload", methods=['POST'])
def upload_files():
    if 'file' not in request.files:
        return 'file not send'
    file = request.files['file']
    if file.filename == '':
        return 'no selected file'
    if file:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return 'file saved successfully'


if __name__ == '__main__':
    app.run(debug=True)
    
