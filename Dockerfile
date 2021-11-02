FROM python:3.8.12-slim

ENV PORT=5000
EXPOSE 5000

# start to install backend-end stuff
RUN mkdir -p /app
WORKDIR /app

# Install Python requirements.
COPY ["Pipfile", "Pipfile.lock", "./"]
RUN pip install pipenv
RUN pipenv install --deploy --system

# Install Python requirements.
COPY ["wine_quality_server.py", "./"]
COPY ["model_classification.bin", "./"]

# Start server
#ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:$PORT", "wine_quality_server:app"]
CMD gunicorn wine_quality_server:app --bind 0.0.0.0:$PORT
