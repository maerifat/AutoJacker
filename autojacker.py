# -*- coding: utf-8 -*-
import os
import sys
if sys.version_info < (3,0,0):
    print(' AutoJack requires Python 3, while Python ' + str(sys.version[0] + ' was detected. Terminating... '))
    sys.exit(1)
import subprocess
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import re
import time
from colorama import Fore, Back, Style


tato= """


     ▄████████ ███    █▄      ███      ▄██████▄            ▄█    ▄████████  ▄████████    ▄█   ▄█▄    ▄████████    ▄████████ 
    ███    ███ ███    ███ ▀█████████▄ ███    ███          ███   ███    ███ ███    ███   ███ ▄███▀   ███    ███   ███    ███ 
    ███    ███ ███    ███    ▀███▀▀██ ███    ███          ███   ███    ███ ███    █▀    ███▐██▀     ███    █▀    ███    ███ 
    ███    ███ ███    ███     ███   ▀ ███    ███          ███   ███    ███ ███         ▄█████▀     ▄███▄▄▄      ▄███▄▄▄▄██▀ 
  ▀███████████ ███    ███     ███     ███    ███          ███ ▀███████████ ███        ▀▀█████▄    ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
    ███    ███ ███    ███     ███     ███    ███          ███   ███    ███ ███    █▄    ███▐██▄     ███    █▄  ▀███████████ 
    ███    ███ ███    ███     ███     ███    ███          ███   ███    ███ ███    ███   ███ ▀███▄   ███    ███   ███    ███ 
    ███    █▀  ████████▀     ▄████▀    ▀██████▀       █▄ ▄███   ███    █▀  ████████▀    ███   ▀█▀   ██████████   ███    ███ 
                                                      ▀▀▀▀▀▀                            ▀                        ███    ███ 
                                        # WhiteHatJr AppSec Team #                                                                                                                                                        

"""
print(Fore.MAGENTA + Style.BRIGHT+tato.center(20))
program1= 'subfinder'
program2 = 'httpx'
check1 = subprocess. run(['which', program1], capture_output=True, text=True)
check2 = subprocess. run(['which', program2], capture_output=True, text=True)
if check1.returncode == 1:
    print('subfinder is not installed. Make sure to run "brew install subfinder" if you are using mac OS.')
    exit()
if check2.returncode == 1:
    print('httpx is not installed. Make sure to run "brew install httpx" if you are using mac OS.')
    exit()
domain = input("Domain: ")
print('Warming up the engine, please wait...')
print()
cmd1 = 'subfinder -d '+domain+' -silent | httpx  -mc 200,301,302,307 -silent > sub_'+domain+'.txt'
results = subprocess.run(
    cmd1, shell=True)
subfile = open('sub_'+domain+'.txt', 'r')
count= 1
vulcount =0
while True:
    try:
        url= str(subfile.readline())
        frame ='x-frame-options'
        res= requests.get(url.strip(), verify=False)
        strheaders = str(res.headers)
        xfo = re.compile(r'(?i)(\'|\")?x-frame-options(\'|\")?(\s)*(\:)(\s)*(\'|\")?(sameorigin|deny)(\'|\")?')
        searched = xfo.search(strheaders)
        strsearched =str(searched)
        if (frame.lower() not in strheaders.lower() ):
            print(Fore.MAGENTA + str(count) + ". " + Fore.RED + url.strip() + " seems Vulnerable." )
            print()
            vulcount +=1
        elif (frame.lower() not in strsearched.lower() and frame.lower() in strheaders.lower() ):
            print(Fore.MAGENTA + str(count) + ". " + Fore.CYAN + url.strip() + " seems Conditional. It needs manual inspection." )
            print()     
        else:
            print(Fore.MAGENTA + str(count) + ". " + Fore.GREEN + url.strip() + " does NOT seem Vulnerable." )
            print()   
    except Exception:
        pass
    count += 1
    if not url:
        break
print(Fore.BLUE + Style.BRIGHT + "Total vulnerable subdomains: " + str(vulcount) )
print()
  
