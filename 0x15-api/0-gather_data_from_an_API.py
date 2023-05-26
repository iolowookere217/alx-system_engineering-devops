#!/usr/bin/python3

"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    # General response
    url = "https://jsonplaceholder.typicode.com"
    user_id = int(sys.argv[1])

    # User endpoint and response
    user_endp = "{}/users/{}".format(url, user_id)
    name = requests.get(user_endp).json().get("name")

    # Task endpoint and response
    task_endp = "{}/todos".format(url)
    tasks = requests.get(task_endp).json()
    tasks_user = [item for item in tasks if item.get("userId") == user_id]
    task_compltd = [item for item in tasks_user if item.get("completed")]
    no_task_done = len(task_compltd)
    total_no_task = len(tasks_user)

    print("Employee {} is done with tasks({}/{}):"
          .format(name, no_task_done, total_no_task))

    for task in task_compltd:
        print("\t{}".format(task.get("title")))
