#!/usr/bin/python3

"""
This is the first file I created for the APIs
"""
import csv
import requests
import sys


def fetch_employee_tasks(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name", "Unknown")

    t_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todo_response = requests.get(t_url)
    todos = todo_response.json()

    with open(f"{employee_id}.csv", "w", newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            taskwriter.writerow([employee_id, employee_name, task.get(
                "completed", False), task.get("title")])

if __name__ == "__main__":
    employee_id = sys.argv[1]
    fetch_employee_tasks(employee_id)
