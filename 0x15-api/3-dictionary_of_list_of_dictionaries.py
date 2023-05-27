#!/usr/bin/python3

"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import json
import requests
import sys

if __name__ == "__main__":
    # General response
    url = "https://jsonplaceholder.typicode.com"

    # User endpoint and response
    user_endp = "{}/users".format(url)
    users = requests.get(user_endp).json()

    # Task endpoint and response
    task_endp = "{}/todos".format(url)
    tasks = requests.get(task_endp).json()

    tasks_user = {
        user.get("id"): [
            {
                "username": user.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed"),
            }
            for task in tasks
            if task.get("userId") == user.get("id")
        ]
        for user in users
    }

    # Saving in json file
    with open("todo_all_employees.json", "w", encoding="utf-8") as file:
        json.dump(tasks_user, file)
