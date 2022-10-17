#!/usr/bin/python3
"""
    A python script that gathers API information, using REST API; url
"""

from requests import get
from json import dump


if __name__ == "__main__":
    user_info = get("https://jsonplaceholder.typicode.com/users/")
    users = user_info.json()

    dict_t = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        response = get(url)
        tasks = response.json()
        dict_t[user_id] = []

        for task in tasks:
            dict_t[user_id].append({
                                "username": username,
                                "task": task.get('title'),
                                "completed": task.get('completed')
                                })
        with open('todo_all_employees.json', 'w') as json_file:
            dump(dict_t, json_file)
