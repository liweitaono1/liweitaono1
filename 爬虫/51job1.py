import os
from bs4 import BeautifulSoup
import re
import requests
from pymysql import *
import job

def request1():
    heading = {
        "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    for i in range(1,2):
        url = 'https://search.51job.com/list/020000,000000,0000,00,9,99,java,2,' + str(i) + '.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
        response = requests.get(url, headers=heading)
        response.encoding = "gbk"
        html_soup = BeautifulSoup(response.text, 'html.parser')
        soup_list = html_soup.find("div",class_="dw_table").find_all("div", class_="el")[1:]
        for x in soup_list:
            title = x.find('a')['title']
            span = x.find('a')
            url = re.search(r'.*?href="(.*?)"', str(span)).group(1)
            company = x.find("span", class_='t2').text
            area = x.find("span", class_="t3").text
            money = x.find('span', class_='t4').text
            day = x.find('span',class_='t5').text
            file_name = '/Users/liweitao/Desktop/1/爬虫/msg/' + company + '.txt'
            # print(file_name)
            try:
                if os.path.exists(file_name):
                    file_name = '/Users/liweitao/Desktop/1/爬虫/msg/' + company + title + '.txt'
                with open(file_name, 'w') as f:
                    f.write(job.main(url))
            except Exception as e:
                print(e)
            conn = connect(host='localhost', user='root', password='liweitao', port=3306, database='zhaoping',charset='utf8')
            cs1 = conn.cursor()
            create_sql = '''create table if not exists 51job(company varchar(200), title varchar(200), money varchar(30), area varchar(200), day varchar(30), url varchar(200), file_name varchar(300));'''
            cs1.execute(create_sql)
            conn.commit()
            insert_sql = '''insert into 51job value('%s','%s','%s','%s','%s','%s', '%s');''' % (company, title, money, area, day, url, file_name)
            cs1.execute(insert_sql)
            conn.commit()
    cs1.close()
    conn.close()


def main():
    request1()


if __name__ == '__main__':
    main()

