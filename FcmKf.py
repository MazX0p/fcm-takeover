import requests
import sys
import random
import re
from shutil import which
from colorama import Fore
import os
import subprocess
import json

def title():
    print('+------------------------------------------')
    print('+  \033[34mScript BY: http://github.com/MazX0p \\ Mohamed Alzhrani                        \033[0m')
    print('+  \033[34mTARGET:  Fcm Server Key Finder and Checker                                 \033[0m')
    print('+  \033[36mUSAGE:  python3 FcmKf.py                                                  \033[0m')
    print('+------------------------------------------')


def apktool(apk):

    url = 'https://fcm.googleapis.com/fcm/send'
    body = {"registration_ids": ["ABC"]}
    headers = {"content-type": 'application/json'}

    try:
        print(Fore.BLUE + f"[+] Decode {os.path.basename(apk)}!")
        os.popen(f"apktool d {apk}").read()
        print(Fore.BLUE + "[+] Apk decoded!")
        print(Fore.YELLOW + "[+] Searching for tokens")
        #apkOutPath = (apk.split('.')[0]+'New')

        apkOutPath = apk.split(".")[0]
        keyword1 = subprocess.getoutput(f'grep -ProIR "AIzaSy[0-9A-Za-z_-]{{33}}" {apkOutPath}')
        keyword2 = subprocess.getoutput(f'grep -ProIR "AAAA[A-Za-z0-9_-]{{7}}:[A-Za-z0-9_-]{{140}}" {apkOutPath}')
        Serverkey = []
        if keyword1:
            fou1 = keyword1.splitlines()
            Serverkey.extend(fou1)
        if keyword2:
            fou12 = keyword2.splitlines()
            Serverkey.extend(fou12)

        if not Serverkey:
            print(Fore.RED + "[-] No tokens found")
            exit()

        tokens1 = [i.split(":")[1] for i in Serverkey]
        print(Fore.BLUE + f"[+] Found tokens: ")
        print(Fore.GREEN + f"[+] {', '.join(list(set(tokens1)))}")
        server_key_p = list(set(tokens1))
        print(Fore.BLUE + "[+] Searching for valid Server Keys")
        headers["Authorization"] = f"key={server_key_p}"
        Test_valid_key = requests.post(url, data=json.dumps(body), headers=headers)
        if Test_valid_key.status_code == 200:
            print(Fore.GREEN + f"[+] {server_key_p}")
            print(Fore.GREEN + f"[+] is a valid server key")
            print(Fore.CYAN + f"[+] Finished!")
        else:
            print(Fore.RED + f"[-] {server_key_p}")
            print(Fore.RED + f"[-] is not a valid server key")
            print(Fore.CYAN + f"[+] Finished!")
    except Exception as e:
        print(Fore.RED + f"[!] Error in validating keys: {e}")

    except Exception as e:
        print(Fore.RED + f"[!] Error in decompiling apk: {e}")



if __name__ == '__main__':
    title()
    Apk_File = str(input("\033[35minput Apk File with path \nApk File   >>> \033[0m"))
    apktool(Apk_File)
