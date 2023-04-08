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

    with open(f"{USER_ID}.csv", mode='w') as f:
        task = csv.writer(f, delimiter=',', quotechar='"',
                          quoting=csv.QUOTE_ALL)
        for i in extract_task:
            # filter by employee ID
            if i.get('userId') == USER_ID:
                TASK_COMPLETED_STATUS = i['completed']
                TASK_TITLE = i['title']
                task.writerow([USER_ID, USERNAME, TASK_COMPLETED_STATUS,
                               TASK_TITLE])
