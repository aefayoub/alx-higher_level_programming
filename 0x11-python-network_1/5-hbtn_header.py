#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests
import sys


if __name__ == "__main__":
    try:
        req = requests.get(sys.argv[1])
        print(req.headers['X-Request-Id'])
    except ex:
        pass
