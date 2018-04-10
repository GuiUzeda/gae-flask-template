# gae-flask-template
This is a simple template to create a web app on Google AppEngine Standard using Flask and Python2.7

## Setup
Since this is to run on the standard mode of GAE, the libraries avalible are limited. The main utilization of this template is to make webapplications which does not require much beyond standard Python and some common libraries such as Numpy.

The Handler code should go on the main.py file and should use the flask model

HTML files should go under the tamplate folder and follow the Jinja2 pattern

Static Files should go each on the respective folder under the static folder

## Usage

To run the flask locally all the requirements should be installed with:

    $ sudo pip install -r requirements.txt

To run on GAE, first install the Google Cloud SDK and initialize it with:

    $ gcloud init

Finally run:
 
    $ gcloud app deploy app.yaml

## Disclaimer

This is not a development repository, it is just a simple template used very oftem by GAE developpers 