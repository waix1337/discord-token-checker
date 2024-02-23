import requests
import colorama
colorama.init()

def checkToken(token):
    r = requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": token})
    return r.status_code

invalid = []

def printResult(status, token):
    if status == 200: 
        color = colorama.Fore.GREEN
        result = "Valid"
    elif status == 429: 
        color = colorama.Fore.YELLOW
        result = "Invalid"
    else: 
        color = colorama.Fore.RED
        result = "Invalid"
        invalid.append(token) 
    print(color + (result) + colorama.Fore.LIGHTBLACK_EX + f" | {token}")

def main():
    tokens = open("tokens.txt", "r").read().splitlines()
    for token in tokens:
        printResult(checkToken(token), token)
    input(colorama.Fore.YELLOW + "[+] Press any key to exit.")

main()