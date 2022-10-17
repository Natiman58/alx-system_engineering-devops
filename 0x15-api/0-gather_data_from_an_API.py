#!/usr/bin/python3
"""
    A python script that gathers API information, using REST API; url
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = get(url)
    name = response.json().get('name')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    response = get(url)
    tasks = response.json()

    total_tasks = []
    completed = 0

    for task in tasks:
        if task.get('completed'):
            total_tasks.append(task)
            completed += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, len(tasks)))

    for task in total_tasks:
        print("\t {}".format(task.get('title')))
