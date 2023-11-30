#!/bin/bash
# SCript shows the response body
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
