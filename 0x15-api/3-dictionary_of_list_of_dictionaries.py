#!/usr/bin/python3
"""This script exports data fetched from an API to a JSON file."""
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = base_url + "users"
    todo_url = base_url + "todos"

    users = requests.get(user_url).json()

    json_file = "todo_all_employees.json"
    with open(json_file, 'w') as f:
        json.dump({
            user.get("id"): [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
                } for todo in requests.get(
                    todo_url, params={"userId": user.get("id")}
                    ).json()]
            for user in users
                }, f)
