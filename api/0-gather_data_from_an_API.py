#!/usr/bin/python3
"""
Script to gather data from the JSONPlaceholder API.

Fetches and displays an employee's TODO list progress.
"""

import requests
import sys


def fetch_employee_data(user_id):
    """Fetch and display the employee's TODO list progress."""
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(
            user_id)).json()
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            user_id)).json()

    completed_tasks = [task for task in todos if task.get('completed')]
    total_tasks = len(todos)
    completed_count = len(completed_tasks)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            user.get('name'), completed_count, total_tasks))
    for task in completed_tasks:
        print("\t " + task.get('title'))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        user_id = sys.argv[1]
        fetch_employee_data(user_id)
    else:
        print("Please provide a valid user ID as an argument.")
