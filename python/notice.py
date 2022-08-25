from asyncio.log import logger
from urllib import request
import requests
import os

line_notify_token = os.environ["LINE_NOTIFY_TOKEN"]
request_headers = {'Authorization': f'Bearer {line_notify_token}'}

def check_line_notify_status():
    """LINE Notify 利用可否検証"""

    line_notify_api = "https://notify-api.line.me/api/status"

    try:
        response = requests.get(line_notify_api, headers = request_headers)
        response.raise_for_status() # If status code is other than 200, flush to exception handling

    except requests.exceptions.RequestException as e:
        print("RequestException for check_line_notify_status. ", e)

    except Exception as e:
        print("An unexpected error occurred while processing 'check_line_notify_status'.", e)

    else:
        print("'check_line_notify_status' was successfully processed.")

    finally:
        print(response.json())
        return response.status_code


def send_line_notify(notification_message):
    """LINE 通知"""

    line_notify_api = "https://notify-api.line.me/api/notify"
    request_body = {'message': f'message: {notification_message}'}

    try:
        response = requests.post(line_notify_api, headers = request_headers, data = request_body)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print("RequestException for send_line_notify. ", e)

    except Exception as e:
        print("An unexpected error occurred while processing 'send_line_notify'.", e)

    else:
        print("'send_line_notify' was successfully processed.")

    finally:
        print(response.json())
        return response.status_code


def main():
    if 200 == check_line_notify_status():
        send_line_notify("test message from python.")


if __name__ == "__main__":
    main()