#! /usr/bin/env python3
# coding: utf-8

import requests

url = "http://0.0.0.0:5000/predict"

wine = [[11.8, 0.51, 0.66, 0.64, 15.0, 0.9973]]
quality = 7

try:
    result = requests.post(url, json=wine).json()
    print(result)
    print(f"The expected result is {quality}")
except Exception as error_msg:
    print(f'AN ERROR OCCURED:\n{error_msg}')
