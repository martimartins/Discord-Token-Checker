######## MADE BY JokeTV#2025 #############

import requests
from os import name, system, path
import threading
import time

accounts_working = []
accounts_not_working = []
counter_working = 0
counter_not_working = 0
status = False

q = "\033[96m[?]\033[0m "
x = "\033[91m[X]\033[0m "
i = "\033[96m[!]\033[0m "

def cls():
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear')

def get_tokens(fpath):
    tokens = []
    with open(fpath, "r") as f:
        for line in f.readlines():
            line = line.replace(" ", "")
            line = line.replace("\r", "")
            line = line.replace("\n", "")

            if (line == ""):
                continue

            tokens.append(line)

    print("Start checking {} tokens...".format(len(tokens)))
    return tokens

def check_token(token):
    global accounts_working
    global counter_working
    global accounts_not_working
    global counter_not_working
    a = requests.get('https://discordapp.com/api/v6/users/@me/library', headers={'authorization': token})
    if a.status_code == 200:
        accounts_working.append(token)
        counter_working += 1
    else:
        counter_not_working += 1
        accounts_not_working.append(token)

if __name__ == '__main__':
    cls()
    print("Discord Token Cheker 1.0\nMade By: JokeTV#2025\n\n")
    q2 = input("{}Which tokens do you want check?[file.txt]: ".format(q))
    if path.exists(q2) is not True:
        while True:
            q2 = input("{}Please put some valid file!: ".format(x))
            if path.exists(q2) is True:
                break
    q1 = input("{}Want to save all the worked tokens at a txt file?[Y/N]: ".format(q)).lower()
    if q1 == "y":
        q3 = input("{}What file u want to save?[file.txt]: ".format(q))
        if path.exists(q2) is not True:
            while True:
                q3 = input("{}Please put some valid file!: ".format(x))
                if path.exists(q2) is True:
                    break
    tokens = get_tokens(q2)
    for token in tokens:
        func = threading.Thread(target=check_token, args=(token,))
        func.start()
        cls()
        print("{}Total checked: {} | Working: {} | Not Working: {}".format(i, counter_working+counter_not_working, counter_working, counter_not_working))
    if q1 == "y":
        with open(q3, 'w+') as f:
            for working in accounts_working:
                f.write("{}\n".format(working))
