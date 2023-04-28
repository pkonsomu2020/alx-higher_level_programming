#!/usr/bin/python3
# script that fetches this url: - https://alx-intranet.hbtn.io/status
import urllib

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body_response = response.read()
        utf8_content = body_response.decode('utf-8')
        print('Body response:')
        print(f'\t- type: {type(body_response)}')
        print(f'\t- content: {body_response}')
        print(f'\t- utf8 content: {utf8_content}')
