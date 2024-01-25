#!/bin/bash
#a bash script that sends a JSON POST request ot a URL passed as the forst argument, and displays the body of the response
curl -sH 'Content-Type: application/json' -d "@${2}" $@
