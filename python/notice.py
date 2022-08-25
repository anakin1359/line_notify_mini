import requests
import os

line_notify_token = os.environ["LINE_NOTIFY_TOKEN"]

def check_line_notify_status():
    """LINE Notifyが利用可能かを検証"""
    line_notify_api = "https://notify-api.line.me/api/status"
    request_headers = {'Authorization': f'Bearer {line_notify_token}'}
    response = requests.get(line_notify_api, headers = request_headers).json()
    status = response["status"]
    return status

def send_line_notify(notification_message):
    """LINEへ通知を行う"""
    line_notify_api = "https://notify-api.line.me/api/notify"
    request_headers = {'Authorization': f'Bearer {line_notify_token}'}
    request_body = {'message': f'message: {notification_message}'}
    response = requests.post(line_notify_api, headers = request_headers, data = request_body).json()
    return response

def main():
    if 200 == check_line_notify_status():
        send_line_notify("test message from python.")
    else:
        print("api request error.")

if __name__ == "__main__":
    main()