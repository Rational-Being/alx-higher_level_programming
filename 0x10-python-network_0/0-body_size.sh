#!/bin/bash
#a bash script that takes in a URL, send a request to the URL, and displays the size of the body of the response
curl -Is "$1" | grep Content-Length | awk '{print $2}'
