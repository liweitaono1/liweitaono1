import multiprocessing
# import gevent
# import re
# import os
import threading
from bs4 import BeautifulSoup
import time
import requests
from urllib.request import *
# from gevent import monkey
# monkey.patch_all()

def see_time(founc):
    def call_founc():
        start_time = time.time()
        founc()
        end_time = time.time()
        run_time = end_time - start_time
        print(run_time)
    return call_founc


def request1():
    heading = {
        "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    url = 'https://www.douyu.com/g_ecy'
    response = requests.get(url, headers=heading)
    response.encoding = "utf-8"
    # print(response.text)
    return response.text



def parse_one_page(html):
    html_soup = BeautifulSoup(html, 'lxml')
    # print(html_soup)
    soup_list = html_soup.find("div", id='live-list-content').find_all("li")
    list = []
    for soup in soup_list:
        c = soup.find("span", class_='imgbox').find('img')['src']
        list.append(c)
        # print(c)
    return list

def save_image(href, name):
    image = urlopen(href)
    with open("./image/%s.png" % name, "wb") as f:
        f.write(image.read())
        print("%s-----------------已下载" % name)

@see_time
def main():
    # num = os.cpu_count()
    html = request1()
    href_list = parse_one_page(html)
    length = len(href_list)
    print(length)
    i = 0
    join_list = []
    for href in href_list:
        i += 1
        threading_a = threading.Thread(target=save_image, args=(href, i))
        threading_a.start()
        # threading_a.join()
        # join_list.append(threading_a)
    # for x in join_list:
    #     x.join()

if __name__ == '__main__':
    main()