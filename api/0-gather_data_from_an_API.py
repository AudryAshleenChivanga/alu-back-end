#!/usr/bin/python3

"""
This is the first file I created for the APIs
"""
import requests
import sys


def fetch_employee_tasks(employee_id):
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name", "Unknown")

    t_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todo_response = requests.get(t_url)
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
    fetch_employee_tasks(employee_id)
