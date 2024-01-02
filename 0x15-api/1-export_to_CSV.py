#!/usr/bin/python3
"""This script returns information about an employee's TO-DO list progress
and exports to a CSV file"""
import csv
import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_url = base_url + '/' + emp_id
    todo_url = user_url + "/todos"

    emp_res = requests.get(user_url)
    emp_username = emp_res.json().get("username")

    task_res = requests.get(todo_url)
    tasks = task_res.json()

    csv_file = emp_id + ".csv"
    # csv_tasks = []
    # for task in tasks:
    #     csv_tasks.append(
    #         [emp_id, emp_username, task.get("completed"), task.get("title")])

    with open(csv_file, 'w') as f:
        # writer = csv.writer(f)
        # writer.writerows(csv_tasks)
        for task in tasks:
            f.write('"{}","{}","{}","{}"\n'.format(
                emp_id, emp_username,
                task.get("completed"), task.get("title")))
