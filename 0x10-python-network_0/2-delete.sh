#!/bin/bash
#a bash scripts that send a DELETE request to the URL passed as the first argument
#and dispalys the body of the response

curl -sX DELETE "$@"