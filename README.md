# Food Vision App

This is a simple temporary app that was used to deploy a ResNet-50 model on Heroku cloud. The model was trained on [Food-101](https://www.kaggle.com/datasets/dansbecker/food-101) dataset from Kaggle.

## Training

The jupyter notebook in this repository contains all the steps I've taken to train the ResNet on this dataset.
The model was only trained for 5 epochs and acheived an accuracy of 76% on test dataset. Further improvement of the accuracy can be made in future releases, but for now I decided to go with this temporarily to set up the DevOps pipeline. 

## App

The app is available on [Heroku](https://food-vision-app.herokuapp.com/). It's likely that you may not find the app to be working as Heroku is a paid platform and I probably ran out of money. :laughing:

### More improvements will be made in the future in all aspects. The website design is rudimentary and I will probably change it into something better soon. Thinking of using a single-page web app in JS instead of plain HTML.