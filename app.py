import torch
import numpy as np
import torchvision.transforms as transforms
from flask import Flask, request, app, jsonify, url_for, render_template, redirect, flash, session, escape
from PIL import Image


app = Flask(__name__)
labels = {}
i=0
with open("labels.txt") as f:
    for line in f:
        labels[i]= line.strip()
        i+=1

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods = ['POST'])
def predict_api():
    model = torch.jit.load('resnet_food.pt', map_location=torch.device('cpu'))
    model.eval()
    data = request.files['image']
    img = Image.open(data.stream)
    print("Img height and img width: ", img.height,img.width)
    transformations = transforms.Compose([transforms.Resize((224,224)),
                                          transforms.ToTensor(),transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
    input_data = transformations(img)
    input_data = input_data.unsqueeze(0)
    output = model(input_data)
    pred = torch.argmax(output)
    conf = torch.max(output)
    result = labels[pred.item()]
    return(jsonify(result,conf.item()*100))



if __name__=='__main__':
    app.run(debug=True)


