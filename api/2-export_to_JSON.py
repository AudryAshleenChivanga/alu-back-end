#!/usr/bin/python3
"""
Module to fetch and export data in the JSON format for a given employee.
"""

import json
import requests
import sys


def fetch_employee_tasks(employee_id):
    """
    Fetch tasks for an employee and write them to a JSON file.

    Args:
    - employee_id: ID of the employee to fetch tasks for.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get("username", "Unknown")

    todo_url = f"{base_url}/todos?userId={employee_id}"
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
    if len(sys.argv) < 2:
        print("Usage: ./script_name.py employee_id")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    fetch_employee_tasks(employee_id)
