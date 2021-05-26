import requests, threading, time, pyfiglet
from bs4 import BeautifulSoup
from random import choice
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import partial
from termcolor import colored

def get_list(session, url):
    get_list = session.get(url).text
    soup = BeautifulSoup(get_list, 'lxml')
    return soup.find('body').get_text().strip()

def recieve_proxies(session, executor):
    link = 'https://api.proxyscrape.com/?request=displayproxies&proxytype=all&timeout=5000&country=all&anonymity=all&ssl=no'
    other = 'https://www.proxy-list.download/api/v1/get?type=http'
    lists = list(executor.map(partial(get_list, session), (link, other)))
    mix = lists[0] + '\n' + lists[1] + '\n'
    raw_proxies = mix.splitlines()
    with open('good_http_proxies.txt', 'a') as outfile:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0","Accept-Encoding": "*","Connection": "keep-alive"}
        session.headers.update(headers)
        futures = {executor.submit(partial(check_http_proxy, session), proxy): proxy for proxy in raw_proxies}
        for future in as_completed(futures):
            proxy = futures[future]


ascii_banner = pyfiglet.figlet_format(f"ProxyProj")
print(ascii_banner)
print(colored("HTTP Proxies", 'red'))
a = input(colored("Press ENTER to continue : ", 'blue'))


def check_http_proxy(session, proxy):
    check = 'http://icanhazip.com'
    try:
        response = session.get(check, proxies={'http': 'http://'+proxy}, timeout=5)
        status = response.status_code
        outfile = open('good_http_proxies.txt', 'a')
        if status == 200:
            print(colored('Working Proxy - '+proxy, 'green'))
            outfile.write(proxy+'\n')
        else:
            return status == 200
    except Exception:
            return False

THREADS=500
with requests.Session() as session:
    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        recieve_proxies(session, executor)



