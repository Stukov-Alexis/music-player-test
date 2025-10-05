from flask import Flask, request, send_from_directory, render_template
import os

app = Flask(__name__)
UPLOAD_FOLDER = "/music"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    songs = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith('.mp3')]
    return render_template('index.html', songs=songs)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if file and file.filename.endswith('.mp3'):
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        return "Upload successful! <a href='/'>Go back</a>"
    return "Invalid file. Only MP3 allowed. <a href='/'>Try again</a>"

@app.route('/music/<filename>')
def get_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
