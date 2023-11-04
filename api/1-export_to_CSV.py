#!/usr/bin/python3
"""
main_1.py: Script to validate the functionality of the script from task #0.
"""

from your_script_name import fetch_employee_data

def validate_employee_data(user_id):
    """Validate the correct retrieval of user ID and username."""
    data = fetch_employee_data(user_id)

    if data:
        user_id_retrieved = data.get('user_id')
        username_retrieved = data.get('username')

        if user_id_retrieved == user_id and username_retrieved:
            print("User ID and Username: OK")
        else:
            print("Username: Incorrect")
    else:
        print("Username: Incorrect")


if __name__ == "__main__":
    user_id_to_test = "2"  # or whatever user ID you want to test
    validate_employee_data(user_id_to_test)
