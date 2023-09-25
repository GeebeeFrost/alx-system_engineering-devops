#!/usr/bin/python3
"""This script returns information about a given employee's
TODO list progress."""
import requests
import sys


if __name__ == "__main__":
    emp_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_url = base_url + '/' + emp_id
    todo_url = user_url + "/todos"

    res = requests.get(user_url)
    emp_name = res.json().get("name")

    res = requests.get(todo_url)
    tasks = res.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get("completed"):
            done += 1
            done_tasks.append(task)

    print("Employee {} is done with tasks({}/{}):".format(
        emp_name, done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
