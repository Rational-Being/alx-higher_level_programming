#!/bin/bash
#a bash script that send a request to a URL passed as anargument
#and siplays only the status code of the response

curl -s -o /dev/null -w "%{http_code}" "$1"