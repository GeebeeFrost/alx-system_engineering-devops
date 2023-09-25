#!/usr/bin/python3
"""This script exports data fetched from an API to a CSV file."""
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
    csv_file = emp_id + ".csv"

    with open(csv_file, 'w') as f:
        for task in tasks:
            f.write('"{}","{}","{}","{}"\n'.format(
                emp_id, emp_name,
                task.get("completed"), task.get("title")))
