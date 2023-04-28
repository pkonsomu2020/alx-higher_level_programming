#!/usr/bin/python3
"""
Script that takes GitHub credentials and uses the GitHub AP
to display the user ID of the authenticated user
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, password))

    try:
        json_data = response.json()
    except ValueError:
        print("Not a valid JSON")
        sys.exit()

    if response.status_code == 200:
        print(json_data.get("id"))
    else:
        print("None")
