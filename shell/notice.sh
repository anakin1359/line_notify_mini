#!/bin/bash

line_notify_token=""

curl -H "Authorization: Bearer ${line_notify_token}" https://notify-api.line.me/api/status |jq
# {
#   "status": 200,
#   "message": "ok",
#   "targetType": "USER",
#   "target": "aaa"
# }

sleep 1s

curl -X POST -H "Authorization: Bearer ${line_notify_token}" -F "message=TEST MESSAGE" https://notify-api.line.me/api/notify |jq
# {
#   "status": 200,
#   "message": "ok"
# }