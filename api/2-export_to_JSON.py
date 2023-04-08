#!/usr/bin/python3
"""
    Write a Python script that, using this REST API,
    for a given employee ID,
    returns information about his/her TODO list progress.
"""


import csv
import json
import requests
import sys


if __name__ == "__main__":
    """user data extraction"""
    USER_ID = int(sys.argv[1])

    api_url = "https://jsonplaceholder.typicode.com/users/{}".format(USER_ID)
    extract_data_employee = requests.get(api_url).json()
    USERNAME = extract_data_employee.get('username')

    """task extraction"""
    task_api_url = "https://jsonplaceholder.typicode.com/todos/"
    extract_task = requests.get(task_api_url).json()

    with open("{}.json".format(USER_ID), "w") as f:
        json.dump({USER_ID: [{
                'task': i.get('title'),
                'completed': i.get('completed'),
                'username': USERNAME
            } for i in extract_task]}, f)
