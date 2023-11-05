#!/usr/bin/python3

"""
The second file using APIs
"""

import csv
import requests
import sys


def fetch_employee_tasks(employee_id):
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get(
        "username", "Unknown")

    t_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todo_response = requests.get(t_url)
    todos = todo_response.json()

    # Create a CSV file and write the tasks data
    with open(f"{employee_id}.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow(
                [employee_id, employee_name, task.get(
                    "completed", False), task.get(
                        "title")])

if __name__ == "__main__":
    # Taking input from the command line
    employee_id = sys.argv[1]
    # Calling the function to fetch and write tasks into a CSV file
    fetch_employee_tasks(employee_id)
