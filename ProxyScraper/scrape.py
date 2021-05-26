import requests, os, time, random, pyfiglet
from colorama import *
from termcolor import colored

ascii_banner = pyfiglet.figlet_format(f"Proxy Scrape")
print(ascii_banner)

esex_https = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=7000&country=ALL&anonymity=elite&ssl=no')
esex_http = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=7000&country=ALL&anonymity=elite&ssl=no')

https = []
https = esex_https.text
https = https.split()
esex_https_lines = len(https)

http = []
http = esex_http.text
http = http.split()
esex_http_lines = len(http)

number = random.randint(1, 5)

def recieve():
    print(colored("[1] HTTPS", 'red'))
    print(colored("[2] HTTP", 'red'))
    print(' ')
    a = input(colored("Select Type of Proxy : ", 'blue'))
    if(a == "1"):
        for i in range(esex_https_lines):
            print(colored(https[i], 'yellow'))
            time.sleep(0.1)
    elif(a == "2"):
        for a in range(esex_http_lines):
            print(colored(http[a], 'yellow'))
            time.sleep(0.1)

if __name__ == "__main__":
    recieve()