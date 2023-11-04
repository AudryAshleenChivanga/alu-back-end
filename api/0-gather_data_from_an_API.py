#!/usr/bin/python3
"""I've created this script to gather data from an API."""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        user_id = sys.argv[1]
        
        # I'm going to fetch the user details using the API.
        user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(user_id)).json()

        # Now, I'll get the list of tasks associated with this user.
        todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)).json()

        # Here, I'm filtering out the completed tasks from the total list.
        completed_tasks = [task for task in todos if task.get('completed')]
        total_tasks = len(todos)
        completed_count = len(completed_tasks)

        # Time to print out the results!
        print("Employee {} is done with tasks({}/{}):".format(user.get('name'), completed_count, total_tasks))
        for task in completed_tasks:
            print("\t " + task.get('title'))

        # This part below is just for the given example. I'll transform spaces and tabs for visualization purposes.
        print("\n" + "-" * 50 + "\n")
        result = "Employee {} is done with tasks({}/{}):\n".format(user.get('name'), completed_count, total_tasks)
        for task in completed_tasks:
            result += "\t " + task.get('title') + "\n"
        print(result.replace(" ", "S").replace("\t", "T"))
    else:
        # If the user forgets to input a valid user ID, I'll remind them.
        print("Please provide a valid user ID as an argument.")

