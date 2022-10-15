import requests
import time

# vars: api endpoint
request_check_endpoint = "https://notify-api.line.me/api/status" # LINE Notify API 利用可否検証
send_notify_endpoint   = "https://notify-api.line.me/api/notify" # LINE 通知

def check_line_notify_request(request_headers):
    """ LINE Notify API 利用可否検証 """

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


def send_line_notify(request_headers, notification_message, file_list):
    """ LINE 通知 """

    endpoint_url = send_notify_endpoint
    request_body = {'message': f'message: {notification_message}'}

    try:
        for file_name in file_list:
            image_convert_dict = {"imageFile": open(f'./img/{file_name}', mode="rb")} # Image file reading -> binaryization -> dictionary format conversion
            response = requests.post(endpoint_url, headers=request_headers, data=request_body, files=image_convert_dict)
            response.raise_for_status()
            print(f'send: ./img/{file_name}')
            time.sleep(0.5)

    except requests.exceptions.RequestException as e:
        print("RequestException for send_line_notify. ", e)

    except Exception as e:
        print("An unexpected error occurred while processing 'send_line_notify'.", e)

    else:
        print("'send_line_notify' was successfully processed.")

    finally:
        print(response.json())
        return response.status_code
