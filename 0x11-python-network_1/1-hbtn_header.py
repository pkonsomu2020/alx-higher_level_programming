#!/usr/bin/python3
"""
Script that takes in a URL, sends a request,
and displays the value of the
variable in the header.
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)
