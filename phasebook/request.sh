#!/bin/bash
helpFunction()
{
    echo ""
    echo "Usage: $0 user_id start_time end_time"
    echo "\tuser_id must be a positive integer"
    echo "\tstart_time must follow the accepted format HH:MM"
    echo "\tend_time must follow the accepted format HH:MM"
    exit 1
}
if [ -z $1 ] || [ -z $2 ] || [ -z $3 ]; then
    helpFunction
else
    curl -H "Content-Type: application/json" -d "{\"start\":  \"$2\", \"end\": \"$3\"}" http://127.0.0.1:5000/schedule/$1
fi
