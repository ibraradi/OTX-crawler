from random import choice
from colorama import Fore
from json import loads
import requests
import sys
# Disable SSL warning
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

w = Fore.WHITE
c = Fore.CYAN
g = Fore.GREEN
r = Fore.RED
y = Fore.YELLOW
colors = [w, c, y, g, r]

def a():
    print(f"""
{choice(colors)}       

#(//(((((#((/((((((((///////////////////////////////////////
#(/((#((((((#((((((((#(((//(/(/(((((//////////////////(///(/
(((#((((##((((///(////(#(((((((((((//(////(/(////////(///(//
(#((##(((((((((/((((((#(((///((//((((/(/(///////(///////(///
(((#####(((((((((((,,,,,,,,,,,,,,,,,,,(/(/((//(///(/(((((((/
(/((((((((######,,,,,,,,,,,,,,,,,,,,,,,,,(((((((((((((((((((
(((((((#((((((&,,,,,,,,,,,,,,,,,,,,,,,,,,,,/((((((((((((((((
((((((((#(((((,,,,,,,,,,,,,,,,,/#(*.,,,,,,,/((((((((///(((((
(((((((###(((((,,,,,,,,,,,*/////.////,,,,,,(((((((((((((((((
#((((#%#(((((((#,,,,,,,,,%//////*/////,,,#((((((((((((((((((
##%#(#(,(((/(((((((&.,,,#@   %&  **%.*#((((((##((((((#(#((((
/((#(*(#(/#(((((((((((((,..    ..,,& .((((((((((((#(((((((((
(((#((,*((,((((((((&,,,@,,,,.*,,,,,,,%#&((((((((((((((((((((
(((((((((((((((((((#*,&,,,,,,,,,,,,,,,##,((#((((((#(((((((((
######################%,,,,,,,,*,,,,,,@###(########(######((
###########################/,.#&,,,,,,######################
###########################%,%###&,/&#######################
###########################%,####################(##########
##########################%#,(##############################
#########################&((#@&#############################
#########################((%((((############################
########################(((&(((&(%##########################
########################%,,(((((*###########################
#%%##%%#%#%#%%##########&,,(((((.%%%%%%%%%%%%%%%%%%%%%%%%%%%
                               
                    Coded By : Ahmed Hesham                       
""")

def otx_crawls(target):
    headers_list = [
        {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"},
        {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    ]
    f_u = open("urls.txt", 'a')
    f_h = open("hostnames.txt", 'r+')
    page = 1
    while True:
        response = loads(requests.get(f"https://otx.alienvault.com/api/v1/indicators/domain/{target}/url_list?limit=500&page={page}", headers=choice(headers_list)).text)
        if not response["paged"] or not response["has_next"]:
            break
        req = response["url_list"]
        for i in req:
            if not i.get("httpcode") in range(499, 599):
                hostname = str(i.get("hostname"))
                if hostname not in f_h.read():
                    f_h.write(hostname + '\n')
                    f_u.write(i.get("url") + '\n')
        page += 1
    f_u.close()
    f_h.close()

a()

for target in open(sys.argv[1],"r").read().split("\n"):
    otx_crawls(target)
    print(f"{y}[*] Total URLs: {len(open('urls.txt', 'r').readlines())}")
    unique_hostnames = set(open('hostnames.txt', 'r').readlines())
    print(f"{y}[*] Total unique hostnames: {len(unique_hostnames)}")
    with open('unique_hostnames.txt', 'a') as f:
        for hostname in unique_hostnames:
            f.write(hostname)
    print(f"{y}[*] Unique hostnames saved to file 'unique_hostnames.txt'.")
