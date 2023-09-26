#!/usr/bin/python3
"""This script exports data fetched from an API to a JSON file."""
import json
import requests
import sys


if __name__ == "__main__":
    emp_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_url = base_url + '/' + emp_id
    todo_url = user_url + "/todos"

    res = requests.get(user_url)
    emp_name = res.json().get("username")

    res = requests.get(todo_url)
    tasks = res.json()

    dic = {emp_id: []}
    for task in tasks:
        dic[emp_id].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": emp_name
            })

    json_file = emp_id + ".json"
    with open(json_file, 'w') as f:
        json.dump(dic, f)
