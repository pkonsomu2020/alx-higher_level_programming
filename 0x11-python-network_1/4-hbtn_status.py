#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

url = 'https://alx-intranet.hbtn.io/status'

response = requests.get(url)

print("Body response:")
print(f"\t- type: {type(response.content)}")
print(f"\t- content: {response.content.decode('utf-8')}")
