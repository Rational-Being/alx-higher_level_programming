#!/bin/bash
#a bash script that takes in a URL as an argument, sends a POST requaest to the URL
#and displays the body of the response

curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"