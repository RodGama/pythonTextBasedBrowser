import os
import sys

import requests
from bs4 import BeautifulSoup
from colorama import init
from colorama import Fore, Back, Style


def cria_arquivo():
    args = sys.argv
    dir_name = args[1]
    tabs_list = []
    if len(args) != 2:
        print('invalid arguments')
        exit()
    _path = f"C:\\Users\\Rodrigo\\PycharmProjects\\Text-Based Browser\\Text-Based Browser\\task\\{dir_name}\\"
    try:
        os.mkdir(f'{_path}')
    except FileExistsError:
        pass
    return _path


def scrape_web_page(r):
    # returns a list of all text on the requested web page
    tags = ['p', 'a', 'ul', 'ol', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    soup = BeautifulSoup(r.content, 'html.parser')
    # get site html
    site_main = soup.children
    html = None
    body = None
    for element in site_main:
        if element.name == 'html':
            html = element
            break
    # get site body
    for element in list(html.children):
        if element.name == 'body':
            body = element
            break
    # resolve all <p> tags and print the text
    all_text = []
    for element in list(body.find_all(tags)):
        all_text.append(element.get_text().strip())
    return all_text


def salva_arquivo(page, pasta, url):
    file_name = url.replace("https://", "")
    aux = file_name.rfind(".")
    file_name = file_name[0:aux]
    if url == "https://2.python-requests.org":
        file_name = "requests"
    with open(pasta + f'/{file_name}.txt', 'w') as f:
        for line in page:
            f.write(line + "\n")


def barra_navegacao(pasta):
    navegacao = []
    url = str(input())
    while url != "exit":
        if url == "exit":
            exit()
        elif url == "back":
            navegacao.pop()
            url = navegacao[len(navegacao) - 1]
        else:
            if not url.startswith("http"):
                try:
                    with open(pasta + url + ".txt") as f:
                        init()
                        print(Fore.BLUE + f.read())
                        f.close()
                        break
                except FileNotFoundError:
                    url = "https://" + url
            if not url.__contains__("."):
                print("URL Incorrect")
                break
            r = requests.get(url)
            if r:
                navegacao.append(r.url)
                page = scrape_web_page(r)
                init()
                for line in page:
                    print(Fore.BLUE + line)
                salva_arquivo(page, pasta, url)
            else:
                print("URL Incorrect")
        url = str(input())


pasta = cria_arquivo()
barra_navegacao(pasta)
