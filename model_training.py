#! /usr/bin/env python3
# coding: utf-8

import pickle
import argparse

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    roc_auc_score,
    f1_score,
    accuracy_score,
    precision_score,
    recall_score,
)


# --- TRAIN ---


def train_model(in_name):

    print(f"Load and prepare data from {in_name}")

    # Load data
    data = pd.read_csv(in_name, sep=";", decimal=".")
    data.columns = data.columns.str.replace(" ", "_").str.lower()

    # Select columns
    selected_columns = [
        "quality",
        "alcohol",
        "volatile_acidity",
        "sulphates",
        "citric_acid",
        "total_sulfur_dioxide",
        "density",
    ]
    df = data[selected_columns]

    # Prepare target
    y_full = df["quality"]

    # Prepare predictors
    dt_full = df.copy()
    dt_full = dt_full.drop(columns="quality")

    # Split the dataset
    dt_train_full, dt_test, y_train_full, y_test = train_test_split(
        dt_full, y_full, test_size=0.2, random_state=42
    )
    dt_train, dt_valid, y_train, y_valid = train_test_split(
        dt_train_full, y_train_full, test_size=dt_test.shape[0], random_state=42
    )

    assert dt_valid.shape[0] == dt_test.shape[0]
    assert dt_full.shape[0] == dt_train.shape[0] + dt_valid.shape[0] + dt_test.shape[0]

    print("Training the model")

    rforest_model = RandomForestClassifier(
        n_estimators=500, random_state=1, n_jobs=-1, max_depth=20
    )
    rforest_model.fit(dt_train_full.values, y_train_full.values)

    evaluate_model(rforest_model, dt_test, y_test)

    return rforest_model


# --- EVALUATE THE MODEL ---


def evaluate_classification(y_true, y_pred, y_pred_proba, multi_class="ovr", verbose=1):
    roc = roc_auc_score(y_true, y_pred_proba, multi_class=multi_class)
    f1 = f1_score(y_true, y_pred, average="weighted")
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average="weighted", zero_division=False)
    recall = recall_score(y_true, y_pred, average="weighted", zero_division=False)
    if verbose > 0:
        print(
            f"ROCAUC:{roc:6.3f} | F1:{f1:6.3f} (precision:{precision:6.3f} & recall:{recall:6.3f}) | Accuracy:{accuracy:6.3f}"
        )
    return roc, f1


def evaluate_model(model, dt_test, y_test):
    print("Evaluating the model")

    y_pred = model.predict(dt_test.values)
    y_pred_proba = model.predict_proba(dt_test.values)
    evaluate_classification(y_test, y_pred, y_pred_proba)


# --- SAVE THE MODEL ---


def save_model(model, out_name):
    print(f"Saving the model as {out_name}")

    with open(out_name, "wb") as f_out:
        pickle.dump((model), f_out)


# --- MAIN FUNCTION ---


if __name__ == "__main__":

    # Initialize arguments parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', type=str, help='The path to the .csv file')
    parser.add_argument('-d', '--destination', type=str, help='The path to model file')
    args = parser.parse_args()

    # Initialize in/out variables
    source = "winequality-red.csv"
    destination = "model_classification_training.bin"
    if(args.source is not None):
        source = args.source
    if(args.destination is not None):
        destination = args.destination

    # Train / Evaluate / Save
    print("Let's train a new model")

    model = train_model(source)
    save_model(model, destination)

    print("Model training complete")
