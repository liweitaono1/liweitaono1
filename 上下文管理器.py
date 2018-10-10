import pymysql

class MyOpen():
    def __init__(self,file ,mode = "r"):
        print("打开文件")
        self.file = file
        self.mode = mode

    def __enter__(self):
        print("返回文件")
        self.content = open(self.file, self.mode)
        # a = "asdc"
        # print(int(a))
        return self.content

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("关闭文件")
        self.content.close()

try:
    with MyOpen("项目.py") as f:
        c = f.read()
        raise SystemError
        print(c)
except:
    pass


class myopen():
    def __init__(self, host1, user1, password1, port1, database1, charset1):
        self.conn = pymysql.connect(host=host1, user=user1, password=password1, port=port1, database=database1, charset=charset1)
        self.cur = self.conn.cursor()
        print("初始化成功")

    def __enter__(self):
        print(1)
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("关闭数据库连接")
        self.cur.close()
        self.conn.close()


host = "localhost"
user = "root"
password = "liweitao"
port = 3306
database = "class"
charset = "utf8"
sql = """select * from stuscore"""
with myopen(host1=host, user1=user, password1=password, port1=port, database1=database, charset1=charset) as f:
    f.execute(sql)
    content = f.fetchall()
    for i in content:
        print(i)




