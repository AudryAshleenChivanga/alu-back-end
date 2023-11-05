#!/usr/bin/python3
"""
Script to gather data from the JSONPlaceholder API.

Fetches and displays an employee's TODO list progress.
"""

import requests
import sys

def fetch_employee_task(employee_id):
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    user_resp = requests.get(user_url)
    user_data = user_resp.json()
    employee_name = user_data.get("name", "Unknown")

    t_ul = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todo_response = requests.get(t_ul)
    todos = todo_response.json()

    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get("completed", False)]
    number_of_done_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))
    for task in completed_tasks:
        print("\t", task.get("title"))


if __name__ == "__main__":
    # Taking input from the command line
    employee_id = sys.argv[1]
    # Calling the fetch_employee function
    fetch_employee_task(employee_id)