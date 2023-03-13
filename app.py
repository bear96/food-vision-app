import torch
import torchvision.transforms as transforms
from flask import Flask, request, app, jsonify, url_for, render_template, redirect, flash, session, escape


app = Flask(__name__)
model = torch.jit.load('resnet_food.pt')
model.eval()


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods = ['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    transformations = transforms.Compose([transforms.Resize((224,224)),
                                          transforms.ToTensor(),transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
    input_data = transformations(data)
    output = model(input_data)
    _, pred = torch.max(output)
    print(pred)
    return(jsonify(pred))




if __name__=='__main__':
    app.run(debug=True)


