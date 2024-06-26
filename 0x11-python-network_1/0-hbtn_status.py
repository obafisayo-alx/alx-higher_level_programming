#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

import urllib.request
import urllib.parse


if __name__ == "__main__":
    with urllib.request.urlopen(
            'https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        print('\t- type:', type(html))
        print('\t- content:', html)
        print('\t- utf8 content:', html.decode('UTF-8'))
