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
    user_id = int(sys.argv[1])

    # User endpoint and response
    user_endp = "{}/users/{}".format(url, user_id)
    username = requests.get(user_endp).json().get("username")

    # Task endpoint and response
    task_endp = "{}/todos".format(url)
    tasks = requests.get(task_endp).json()

    tasks_user = {
        user_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username,
            }
            for task in tasks
            if task.get("userId") == user_id
        ]
    }

    # Saving in JSON file
    with open("{}.json".format(user_id), "w", encoding="utf-8") as file:
        json.dump(tasks_user, file)
