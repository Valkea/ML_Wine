## Summary

This project is the Midterm project for the ML-bookcamp (with Alexey Grigorev).
The goal is to gather some experience in various steps of ML pipeline.

With this in mind, I made Explaratory Data Analysis on several datasets (such as Chess-games, Respiratory Syndroms, Allergy Syndroms), but they required more time than expected... 

So, I finally selected a Wine dataset because it offered the possibility to train it as a Regression or as a Classification.

---

Using this dataset, I will try build a model that can predict the wine "quality" based upon some physicochemical information.

Such projects can probably be used by Wine industry companies in order to adjust their products.
Also, this can be used to estimate the probability to get a quality rate for a given product before asking for an expensive certification.

### Dataset source

- https://archive.ics.uci.edu/ml/datasets/Wine+Quality
- https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv
- https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv





## Running locally using python scripts

Install pipenv
```bash
>> pip install pipenv
```

Start the pipenv virtual environment:
```bash
>> pipenv shell
```

Install the dependencies:
```bash
(venv) >> pipenv install
```

Start Flask development server:
```bash
(venv) >> python wine_quality_server.py
```


### Tests
One can check that the server is running by opening the following url:
http://0.0.0.0:5000

Once the wine-server is running, one can send a prediction request as follows:
```bash
>> python wine_quality_client.py
```
This should return a wine-quality of 7

## Docker

### Building a Docker image

```bash
docker build -t wine-quality-prediction .
```

### Running a local Docker image

```bash
docker run -it -p 5000:5000 wine-quality-prediction:latest
```

Then one can run the same test steps as before... (open url and run wine_quality_client.py)

### Pulling a Docker image from Docker-Hub

I pushed a copy of my docker image on the Docker-hub, so one can pull it:

```bash
docker pull valkea/wine-quality-prediction:latest
```

But this command is optionnal, as running it (see below) will pull it if required.

### Running a Docker image gathered from Docker-Hub

Then the command to start the docker is almost similar to the previous one:

```bash
docker run -it -p 5000:5000 valkea/wine-quality-prediction:latest
```

And once again, one can run the same test steps explained above... (open url and run wine_quality_client.py)
