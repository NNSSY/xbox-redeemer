import requests
import random
import threading
import sys
from colorama import Fore
import random

def delete_multiple_lines(number):
    for i in range(number):
        sys.stdout.write("\x1b[1A") 
        sys.stdout.write("\x1b[2K") 
      


WLID = input("What is your WLID?\n")
delete_multiple_lines(100)
with open('fetched/WLID.txt', 'w') as negro:
  negro.write(WLID)

proxies_list = open("fetched/proxies.txt", "r").read().splitlines()


def delete_multiple_lines(number):
    for i in range(number):
        sys.stdout.write("\x1b[1A") 
        sys.stdout.write("\x1b[2K") 

def delete_text(code):
  with open("fetched/accs.txt", "r") as f:
    lines = f.readlines()
  with open("fetched/accs.txt", "w") as f:
    for line in lines:
        if line.strip("\n") != code:
            f.write(line)

def microsoft(code):
    WLID = open('fetched/WLID.txt','r').read()
    proxy = random.choice(proxies_list)
    URL = "https://purchase.mp.microsoft.com/v7.0/tokenDescriptions/" + code
    Payload = {
               'market': 'US', 
               'language': 'en-US', 
               'supportMultiAvailabilities': 'true'
              }
  
    Headers = {
               'Host': 'purchase.mp.microsoft.com', 
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0', 
               'Accept': 'application/json, text/javascript, */*; q=0.01', 
               'Accept-Language': 'en-US,en;q=0.5', 
               'Accept-Encoding': 'gzip, deflate', 
               'Referer': 'https://www.microsoft.com/', 
               'MS-CV': 'QwpC4ofKMEC+vtuT.1.0.6.7', 
               'Authorization': f'{WLID}', 
               'Origin': 'https://www.microsoft.com',
               'Connection': 'close'
              }
   
    try:
     r = requests.get(URL, params=Payload, headers=Headers, proxies={"http": proxy, "https": proxy})
    except:
     r = requests.get(URL, params=Payload, headers=Headers)
    if r.status_code == requests.codes.ok:
        print("[" + Fore.BLUE + "-" + Fore.WHITE + "]" + Fore.MAGENTA + "Redeemed Successfully!\n> " + Fore.WHITE)
    else:
        print("[" + Fore.RED + "-" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + "Redeem Fail!" + Fore.WHITE)
    delete_text(code)
    with open('fetched/redeemed.txt', 'a') as w:
      w.write(code + '\n')
    
 

codes = open('fetched/accs.txt', 'r').read().splitlines()
for code in codes:
  t = threading.Thread(target=microsoft, args=(code,))
  t.start()
  while threading.active_count() >= 45:
      t.join()
