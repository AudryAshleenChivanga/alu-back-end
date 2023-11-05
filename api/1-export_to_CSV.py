#!/usr/bin/python3
"""
Script to gather data from the JSONPlaceholder API and export to CSV.

Fetches and exports an employee's TODO list.
"""


import csv
import requests
import sys


def fetch_employee_data(user_id):
    """Fetch and export the employee's TODO list to CSV."""
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(
            user_id)).json()
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            user_id)).json()

    with open('{}.csv'.format(user_id), 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            csv_writer.writerow(
                [user_id, user.get('name'), task.get(
                    'completed'), task.get('title')])

    print("Data exported to {}.csv".format(user_id))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        user_id = sys.argv[1]
        fetch_employee_data(user_id)
    else:
        print("Please provide a valid user ID as an argument.")
