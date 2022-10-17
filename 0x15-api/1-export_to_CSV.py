#!/usr/bin/python3
"""
    A python script that gathers API information, using REST API; url
"""

from requests import get
from sys import argv
import csv


if __name__ == "__main__":
    user_id = argv[1]
    user_info = get("https://jsonplaceholder.typicode.com/users/{}"
                    .format(user_id))
    user_name = user_info.json().get('username')

    todos = get('https://jsonplaceholder.typicode.com/todos')
    tasks = todos.json()

    file_name = user_id + '.csv'
    with open(file_name, mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in tasks:
            if task.get('userId') == int(user_id):
                writer.writerow([user_id, user_name, task.get('completed'),
                                 task.get('title')])
