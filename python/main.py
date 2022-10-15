import util.notice as notice
import os

# vars: api basic
line_notify_token = os.environ["LINE_NOTIFY_TOKEN"]
request_headers = {'Authorization': f'Bearer {line_notify_token}'}
send_message = "test message from python."

def main():
    """ Exec LINE Notify API """
    if 200 == notice.check_line_notify_request(request_headers):
        notice.send_line_notify(request_headers, send_message)

if __name__ == "__main__":
    main()