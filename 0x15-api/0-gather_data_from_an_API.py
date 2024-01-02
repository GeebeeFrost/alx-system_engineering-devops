#!/usr/bin/python3
"""This script returns information about an employee's TO-DO list progress"""
import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_url = base_url + '/' + emp_id
    todo_url = user_url + "/todos"

    emp_res = requests.get(user_url)
    emp_name = emp_res.json().get("name")

    task_res = requests.get(todo_url)
    tasks = task_res.json()
    done = 0
    tasks_done = []

    for task in tasks:
        if task.get("completed"):
            done += 1
            tasks_done.append(task)

    print("Employee {} is done with tasks({}/{})".format(
        emp_name, done, len(tasks)
    ))
    for task in tasks_done:
        print("\t {}".format(task.get("title")))
