#!/bin/bash
# script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
culr -sX DELETE "$1"
