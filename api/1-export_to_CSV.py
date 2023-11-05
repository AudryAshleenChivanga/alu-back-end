#!/usr/bin/python3
"""
Script to gather data from the JSONPlaceholder API.

Fetches and displays an employee's TODO list progress and exports to a CSV file.
"""


import csv
import requests
import sys


BASE_URL = 'https://jsonplaceholder.typicode.com'

def fetch_employee_data(user_id):
    """Fetch and display the employee's TODO list progress and write to CSV."""
    user = requests.get(f'{BASE_URL}/users/{user_id}').json()
    todos = requests.get(f'{BASE_URL}/todos?userId={user_id}').json()

    # Write to CSV file
    with open(f'{user_id}.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            csv_writer.writerow(
                [user_id, user.get(
                    'name'), task.get('completed'), task.get('title')])

    # Display progress as before
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
