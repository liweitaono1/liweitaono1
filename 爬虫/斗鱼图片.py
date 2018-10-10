import multiprocessing
import gevent
import re
import os
import threading
from bs4 import BeautifulSoup
import time
import requests
from urllib.request import *
import shutil
# from gevent import monkey
# monkey.patch_all()


def see_time(founc):
    def call_founc():
        start_time = time.time()
        founc()
        end_time = time.time()
        run_time = end_time - start_time
        print(int(run_time))
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
    html_soup = BeautifulSoup(html, 'xml')
    # print(html_soup)
    soup_list = html_soup.find("div", id='live-list-content').find_all("li")
    list = []
    for soup in soup_list:
        try:
            c = soup.find("span", class_='imgbox').find('img')['data-original']
            list.append(c)
            # print(c)
        except Exception as e:
            print(e)
    # print(len(list))
    return list


def save_image(href_list, name):
    for href in href_list:
        name += 1
        print(href)
        g = threading.Thread(target=deal, args=(href, name))
        g.start()
        g.join()


def deal(href, name):
    image = urlopen(href)
    with open("./image/%s.jpg" % name, "wb") as f:
        f.write(image.read())
        print("%s-----------------已下载" % name)


@see_time
def main():
    num = os.cpu_count()
    print(num)
    start_page = 0
    # multiprocessing.Pool(num)
    html = request1()
    href_list = parse_one_page(html)
    length = len(href_list)
    print(length)
    c = int(length/num)
    end_page = c
    print(end_page)
    start_page_p2 = start_page + c
    end_page_p2 = end_page + c
    start_page_p3 = start_page_p2 + c
    end_page_p3 = end_page_p2 + c
    start_page_p4 = start_page_p3 + c
    end_page_p4 = end_page_p3 + c
    name1 = 0
    name2 = 51
    name3 = 101
    name4 = 150
    p_1 = multiprocessing.Process(target=save_image, args=(href_list[start_page:end_page], name1))
    p_2 = multiprocessing.Process(target=save_image, args=(href_list[start_page_p2:end_page_p2], name2))
    p_3 = multiprocessing.Process(target=save_image, args=(href_list[start_page_p3:end_page_p3], name3))
    p_4 = multiprocessing.Process(target=save_image, args=(href_list[start_page_p4:end_page_p4], name4))

    p_1.start()
    p_2.start()
    p_3.start()
    p_4.start()
    p_1.join()
    p_2.join()
    p_3.join()
    p_4.join()
    # # threading_a = threading.Thread(target=save_image, args=(href, i))
    # # threading_a.start()
    # i += 1



if __name__ == '__main__':
    if os.path.exists("./image"):
        shutil.rmtree("./image")
    else:
        os.mkdir("image")
    main()