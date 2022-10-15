from asyncio.log import logger
from operator import mod
from urllib import request
import requests
import os

# vars: api basic
line_notify_token = os.environ["LINE_NOTIFY_TOKEN"]
request_headers = {'Authorization': f'Bearer {line_notify_token}'}

# vars: api endpoint
request_check_endpoint = "https://notify-api.line.me/api/status" # LINE Notify API 利用可否検証
send_notify_endpoint   = "https://notify-api.line.me/api/notify" # LINE 通知

def check_line_notify_request():
    """LINE Notify API 利用可否検証"""

    endpoint_url = request_check_endpoint

    try:
        response = requests.get(endpoint_url, headers=request_headers)
        response.raise_for_status() # If status code is other than 200, flush to exception handling

    except requests.exceptions.RequestException as e:
        print("RequestException for check_line_notify_request. ", e)

    except Exception as e:
        print("An unexpected error occurred while processing 'check_line_notify_request'.", e)

    else:
        print("'check_line_notify_request' was successfully processed.")

    finally:
        print(response.json())
        return response.status_code


def send_line_notify(notification_message): # http status code を返却
    """LINE 通知"""

    endpoint_url = send_notify_endpoint
    request_body = {'message': f'message: {notification_message}'}
    send_image_file = {"imageFile": open("./img/Potter_1.jpg", mode="rb")} # Image file reading -> binaryization -> dictionary format conversion

    try:
        response = requests.post(endpoint_url, headers=request_headers, data=request_body, files=send_image_file)
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
    if 200 == check_line_notify_request():
        send_line_notify("test message from python.")


if __name__ == "__main__":
    main()