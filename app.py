#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import speech_recognition as sr

app = Flask(__name__)

@app.route("/")
def index():
    return(render_template("index.html"))

@app.route("/predict", methods=["GET","POST"])
def predict():
    if request.method=="POST":
        file = request.files["file"]
        print("file received")
        filename = secure_filename(file.filename)
        print(filename)
        file.save("static/"+filename)
        a = sr.AudioFile("static/"+filename)
        with a as source:
            a = sr.Recognizer().record(source)
        s = sr.Recognizer().recognize_google(a)
        return(render_template("index.html", result=s))
    else:
        return(render_template("index.html", result="2"))
    
if __name__=="__main__":
    app.run()

