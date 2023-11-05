#!/usr/bin/python3


"""
Using what you did in the task #0, extend your 
Python script to export data in the JSON format.
"""
import json
import requests
import sys

def fetch_employee_tasks(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get("username", "Unknown")

    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todo_response = requests.get(todo_url)
    todos = todo_response.json()

    tasks_list = []
    for task in todos:
        task_data = {
            "task": task.get("title"),
            "completed": task.get("completed", False),
            "username": username
        }
        tasks_list.append(task_data)

    with open(f"{employee_id}.json", "w") as jsonfile:
        json.dump({employee_id: tasks_list}, jsonfile)

if __name__ == "__main__":
    employee_id = sys.argv[1]
    fetch_employee_tasks(employee_id)
