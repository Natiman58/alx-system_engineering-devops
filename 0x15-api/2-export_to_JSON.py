#!/usr/bin/python3
"""
    A python script that gathers API information, using REST API; url
"""

from requests import get
from sys import argv
from json import dump


if __name__ == "__main__":
    user_id = argv[1]
    user_info = get("https://jsonplaceholder.typicode.com/users/{}"
                    .format(user_id))
    user_name = user_info.json().get('username')

    todos = get('https://jsonplaceholder.typicode.com/todos')
    tasks = todos.json()

    dict_t = {user_id: []}

    for task in tasks:
        dict_t[user_id].append({
                                "task": task.get('title'),
                                "completed": task.get('completed'),
                                "username": user_name
                                })
    file_name = user_id + '.json'
    with open(file_name, "w") as json_file:
        dump(dict_t, json_file)
