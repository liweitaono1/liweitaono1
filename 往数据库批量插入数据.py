import pymysql


def main():
    conn = pymysql.connect(host="localhost", database="python_test_1", user="root", password="liweitao", charset="utf8", port=3306)
    cursor = conn.cursor()
    for x in range(10000):
        sql = """insert into test_index(title) values("h%d")"""%x
        cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()




import pymysql
conn = pymysql.connect(host="localhost", port=3306, database="python_test_1", user="root", password="liweitao", charset="utf8")
coursor = conn.cursor()
sql = """select count(*) from test_index"""
a = coursor.execute(sql)
print(coursor.fetchall())
coursor.close()
conn.close()


