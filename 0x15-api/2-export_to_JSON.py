#!/usr/bin/python3
"""This script returns information about an employee's TO-DO list progress
and exports to a JSON file"""
import json
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

    emp_dict = {emp_id: []}
    for task in tasks:
        emp_dict[emp_id].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": emp_username
        })

    json_file = emp_id + ".json"
    with open(json_file, 'w') as f:
        json.dump(emp_dict, f)
