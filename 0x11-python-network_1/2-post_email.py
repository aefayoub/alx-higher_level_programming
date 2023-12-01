#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    emails = {'email': sys.argv[2]}
    data = parse.urlencode(emails)
    data = data.encode('ascii')
    requestdata = request.Request(sys.argv[1], data)
    with request.urlopen(requestdata) as response:
        body = response.read()
        print(body.decode('utf-8'))
