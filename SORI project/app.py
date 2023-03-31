from flask import Flask, render_template, request, redirect, url_for, session , send_file
import subprocess
import os 
import cv2
from PIL import Image
import cv2
import re
import requests
import json
import io
import wave
from ocr import final
import shutil


app = Flask(__name__)
app.config['SECRET_KEY'] = 'magicmagicmagic'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

shutil.rmtree('C:/Users/student/project/testcam/runs/detect', ignore_errors=True)
static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
os.makedirs(os.path.join(static_folder, 'uploads'), exist_ok=True)


@app.route('/')
def index():
    return render_template('indexi.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = file.filename
    file_path = os.path.join(static_folder, 'uploads', filename)
    file.save(file_path)
    session['image_path'] = file_path
    return redirect(url_for('detect_view'))




@app.route('/detect')
def detect_view():
    image_path = session.get('image_path')
    if not image_path:
        return redirect(url_for('upload_view'))
    audio_file, text_result, image_urls = detect(image_path)
    return render_template('index.html', audio_file=audio_file, text_result=text_result , image_urls = image_urls)


def detect(image_path):
    filename = os.path.basename(image_path)
    session['image_filename'] = filename  

    cmd = f"python detect.py --weights best.pt --source {image_path} --save-crop"
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output, _ = p.communicate() # yolov5 
    
    detect_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'runs', 'detect', 'photo')
    image_urls = [f"http://127.0.0.1:5000/static/uploads/{file}" for file in os.listdir(detect_folder) if file.endswith('.jpg')]
    
    text_list = final()  
    new_list = " ".join(text_list)
   

    url = "http://localhost:8080/synthesize" # voice
    data = {'text': new_list}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    container_name_or_id = 'sori'
    local_file_path = 'C:/Users/student/project/testcam/'
    cmd = f"docker cp {container_name_or_id}:/app/static {local_file_path}"
    subprocess.call(cmd, shell=True)
    image_file_path = image_path
    
    return ('./static/audio.wav', new_list, image_urls)



if __name__ == '__main__':
     app.run(debug=True)