#!/usr/bin/python3
"""
Script to export an employee's TODO list to CSV from the JSONPlaceholder API.
"""

import csv
import requests
import sys


def export_to_csv(user_id):
    """Export tasks of the given employee to a CSV file."""
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(user_id)).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)).json()

    with open('{}.csv'.format(user_id), 'w', newline='') as csvfile:
        task_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        
        for task in todos:
            task_writer.writerow([user_id, user.get('name'), task.get('completed'), task.get('title')])


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        user_id = sys.argv[1]
        export_to_csv(user_id)
    else:
        print("Please provide a valid user ID as an argument.")
