from bs4 import BeautifulSoup
import re
import os
import time
import requests
import gevent
from gevent import monkey
import multiprocessing
from pymysql import *

def request1():
    url_list = []
    heading = {
        "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    for i in range(1,368):
        url = 'https://search.51job.com/list/020000,000000,0000,00,9,99,java,2,' + str(i) + '.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
        response = requests.get(url, headers=heading)
        response.encoding = "gbk"
        url_list.append(response.text)
    return url_list

def parse_one_page(html_list):
    info_list = []
    for html in html_list:
        # print(html)
        html_soup = BeautifulSoup(html, 'html.parser')
        soup_list = html_soup.find("div",class_="dw_table").find_all("div", class_="el")[1:]
        for x in soup_list:
            info_list1 = {}
            title = x.find('a')['title']
            span = x.find('a')
            url = re.search(r'.*?href="(.*?)"', str(span)).group(1)
            company = x.find("span", class_='t2').text
            area = x.find("span", class_="t3").text
            money = x.find('span', class_='t4').text
            day = x.find('span',class_='t5').text
            info_list1['money'] = money
            info_list1['day'] = day
            info_list1['area'] = area
            info_list1['company'] = company
            info_list1['url'] = url
            info_list1['title'] = title
            info_list.append(info_list1)
    # for y in info_list:
    #     print(y)
    # print(info_list)
    return info_list

def fangrushujuku(info_list):
    conn = connect(host='localhost', user='root', password='liweitao', port=3306, database='zhaoping', charset='utf8')
    cs1 = conn.cursor()
    create_sql = '''create table if not exists 51job(company varchar(200), title varchar(200), money varchar(30), area varchar(200), day varchar(30), url varchar(200));'''
    cs1.execute(create_sql)
    conn.commit()
    try:
        for x in info_list:
            company = x['company']
            money = x['money']
            url = x['url']
            title = x['title']
            day = x['day']
            area = x['area']
            insert_sql = '''insert into 51job(company,title,money,area,day,url) value('%s','%s','%s','%s','%s','%s');''' % (company, title, money, area, day, url)
            cs1.execute(insert_sql)
            conn.commit()
    except Exception as e:
        print(e)
    finally:
        cs1.close()
        conn.close()


def main():
    html_list = request1()
    # parse_one_page(html_list)
    info_list = parse_one_page(html_list)
    fangrushujuku(info_list)

if __name__ == '__main__':
    main()