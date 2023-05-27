#!/usr/bin/python3

"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import csv
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

    user_tasks = [
        [user_id, username, task.get("completed"), task.get("title")]
        for task in tasks
        if user_id == task.get("userId")
    ]

    # Saving in CSV file
    with open("{}.csv".format(user_id), "w", newline='') as file:
        writer = csv.writer(file)
        for row in user_tasks:
            writer.writerow(row)
