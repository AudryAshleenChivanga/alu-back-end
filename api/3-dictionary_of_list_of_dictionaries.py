#!/usr/bin/python3

"""
Using what you did in the task #0, extend your
Python script to export data in the JSON format.
"""


import json
import requests

def fetch_all_tasks_for_all_users():
    # Base URLs
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetching users and todos data
    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    user_task_dict = {}

    for user in users:
        user_id = user["id"]
        user_name = user["username"]
        user_tasks = [
            {
                "username": user_name,
                "task": todo["title"],
                "completed": todo["completed"]
            }
            for todo in todos if todo["userId"] == user_id
        ]
        user_task_dict[str(user_id)] = user_tasks

    with open("todo_all_employees.json", "w") as outfile:
        json.dump(user_task_dict, outfile, indent=4)

# Call the function
fetch_all_tasks_for_all_users()
