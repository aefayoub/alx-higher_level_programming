#!/bin/bash
# Script shows the content-length
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
