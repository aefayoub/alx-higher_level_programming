#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
from requests import get, auth
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    user = sys.argv[1]
    password = sys.argv[2]
    req = get(url, auth=auth.HTTPBasicAuth(user, password))
    print(req.json().get('id'))
