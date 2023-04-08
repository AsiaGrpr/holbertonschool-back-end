#!/usr/bin/python3
"""
    Write a Python script that, using this REST API,
    for a given employee ID,
    returns information about his/her TODO list progress.
"""


import json
import requests


if __name__ == '__main__':
    """user data extraction"""
    extract_data = "https://jsonplaceholder.typicode.com/users/"
    extract_employee = requests.get(extract_data).json()

    """task extraction"""
    task_api_url = "https://jsonplaceholder.typicode.com/todos"
    extract_task = requests.get(task_api_url).json()

    filename = "todo_all_employees.json"
    with open(filename, "w") as f:
        """dict"""

        dict_task = {i.get("id"): [{
            'task': j.get('title'),
            'completed': j.get('completed'),
            'username': i.get('username')}
            for j in extract_task
            if i.get("id") == j.get('userId')]
            for i in extract_employee}

        json.dump(dict_task, f)
