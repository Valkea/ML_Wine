## Summary

This project is the Midterm project for the ML-bookcamp (with Alexey Grigorev).
The goal is to gather some experience in various steps of ML pipeline.

With this in mind, I made Explaratory Data Analysis on several datasets (such as Chess-games, Respiratory Syndroms, Allergy Syndroms), but they required more time than expected... 

So, I finally selected a Wine dataset because it offered the possibility to train it as a Regression or as a Classification.
(I developped both EDA, but the main one is the Classification EDA)

---

Using this dataset, I will try build a model that can predict the wine "quality" based upon some physicochemical information.

Such projects can probably be used by Wine industry companies in order to adjust their products.
Also, this can be used to estimate the probability to get a quality rate for a given product before asking for an expensive certification.

### Dataset source

- https://archive.ics.uci.edu/ml/datasets/Wine+Quality
- https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv
- https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv


## Cloud demo

One can try the application here:
https://ml-wine.herokuapp.com/input


## Clone repo

```bash
>> git clone https://github.com/Valkea/ML_Wine 
>> cd ML_Wine
```

## Running jupyter-notebook


```bash
>> jupyter notebook
or
>> jupyter notebook "EDA - Wine - Multiclass Classification.ipynb"
or
>> jupyter notebook "EDA - Wine - Multiclass Regression.ipynb"
```

This project focused on the Classification problem, then it was declined on the Regression problem.
The two EDA's selected different models, but the Regression EDA is basically a clone of the Classification EDA with some minor changes (so you don't really need to read both).

The model (model_classification.bin) served by Flask was created using the Classification EDA, but both models can be tested using the 'Load Models.ipynb' notebook.

Also, the notebook was formated using some HTML, and the GitHub preview doesn't render all of them.

## Running locally using python scripts

Install pipenv
```bash
>> pip install pipenv
```

Start the pipenv virtual environment:
```bash
>> pipenv shell
```
*(If it doesnt' work due to the Python 3.8 requirement, you can edit the Pipfile with you own version. I think it should work with any Python3 version has I didn't used any specific function or method.)*

Install the dependencies:
```bash
(venv) >> pipenv install
```

Start Flask development server:
```bash
(venv) >> python wine_quality_server.py
```

Stop with CTRL+C


### Tests
One can check that the server is running by opening the following url:
http://0.0.0.0:5000/input

Then by submitting various physicochemical configurations, various results should be displayed.

Alternatively a python script can be used to test from 'outside' of the Flask app.
```bash
>> python wine_quality_client.py
```
This should return a wine-quality of 7

## Docker

### Building a Docker image

```bash
>> docker build -t wine-quality-prediction .
```

### Running a local Docker image

```bash
>> docker run -it -p 5000:5000 wine-quality-prediction:latest
```

Stop with CTRL+C

Then one can run the same test steps as before... (open input url or run wine_quality_client.py)

### Pulling a Docker image from Docker-Hub

I pushed a copy of my docker image on the Docker-hub, so one can pull it:

```bash
>> docker pull valkea/wine-quality-prediction:latest
```

But this command is optionnal, as running it (see below) will pull it if required.

### Running a Docker image gathered from Docker-Hub

Then the command to start the docker is almost similar to the previous one:

```bash
>> docker run -it -p 5000:5000 valkea/wine-quality-prediction:latest
```

Stop with CTRL+C

And once again, one can run the same test steps explained above... (open input url or run wine_quality_client.py)


## Create a new model file from python script

In order to create a new model .bin file, one can use the following command:

```bash
>> python model_training.py
```
This will use the default input and out names. But this can be changed using the -s (--source) and -d (--destination) parameters.

```bash
>> python model_training.py -s in.csv -d out.bin
```

## Cloud deployement

In order to deploy this project, I decided to use Heroku.

So if you don't already have an account, you need to create one and to follow the process explained here: https://devcenter.heroku.com/articles/heroku-cli

Once the Heroku CLI is configured, one can create a project using the following command (or their website):

```bash
>> heroku create ml-wine
```

Then, the project can be compiled, published and ran on Heroku, with:

```bash
>> heroku container:push web -a ml-wine
>> heroku container:release web -a ml-wine
```

Finally, you can open the project url (mine is https://ml-wine.herokuapp.com/input), or check the logs using:
```bash
>> heroku logs --tail --app ml-wine
```

Finally, here is a great ressource to help deploying projects on Heroku:
https://github.com/nindate/ml-zoomcamp-exercises/blob/main/how-to-use-heroku.md
