#!/usr/bin/python3
"""
    Write a Python script that, using this REST API,
    for a given employee ID,
    returns information about his/her TODO list progress.
"""


import json
import requests
import sys


if __name__ == "__main__":
    """ define variables"""
    TASK_TITLE = []
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0

    """user data extraction"""
    emp_id = int(sys.argv[1])
    api_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    extract_data_employee = requests.get(api_url).json()
    EMPLOYEE_NAME = extract_data_employee.get('name')

    """task extraction"""
    task_api_url = "https://jsonplaceholder.typicode.com/todos/"
    extract_task = requests.get(task_api_url).json()

    for data in extract_task:
        if data.get('userId') == emp_id:
            if data.get('completed') is True:
                TASK_TITLE.append(data['title'])
                NUMBER_OF_DONE_TASKS += 1
            TOTAL_NUMBER_OF_TASKS += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for task in TASK_TITLE:
        print("\t {}".format(task))
