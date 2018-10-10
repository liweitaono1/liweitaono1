from pymysql import *

class Fields(object):
    def __init__(self,file_type):
        self.file_type = file_type

class CreateClass(type):
    def __new__(cls, class_name, super_name, attrs):
        print(attrs)

        # 判断当前的值如果是元组,就组成一个新的字典
        create_params = dict()

        # 从原先的字典中取出来
        for key, value in attrs.items():
            # 判断是否是元组
            if isinstance(value,Fields):
                # 需要的数据添加进去
                create_params[key] = value.file_type # 取到真实的数据

        # 在原先的字典中添加我们新的字典
        attrs['create_params'] = create_params
        # 拿到类名
        attrs['table_name'] = class_name.lower()

        print(create_params)
        return type.__new__(cls, class_name, super_name, attrs)


class Createtable(object, metaclass=CreateClass):
    # uid = ("int unsigned",)
    # name = ("varchar(30)",)
    # email = ("varchar(30)",)
    # password = ("varchar(30)",)

    # uid = Fileld("int unsigned")
    # name = Fileld("varchar(30)")
    # email = Fileld("varchar(30)")
    # password = Fileld("varchar(30)")
    def create_table(self):
        """创建数据库表"""

        # 1.连接数据库
        # 创建connection连接
        conn = connect(host="localhost", port=3306, database="stock_db", user='root', password='liweitao', charset='utf8')
        # 获得cursor对象
        cs1 = conn.cursor()
        # 2.执行sql语句
        # 里面的所有字段使用字段生成
        # create_dict = {"uid":'int unsigned','name':'varchar(30)','password':'varchar(30)','class_name':'varchar(30)'}
        # 循环去得到字符串
        # 存在列表里
        fields = list()

        for key,value in self.create_params.items():
            fields.append("%s %s" %(key,value))
            print(fields)
        # create_sql = """create table if not exists user(uid int unsigned,name varchar(30),email varchar(30),password varchar(30));"""
        create_sql = """create table if not exists %s (%s);""" % (self.table_name,",".join(fields)) # "."join这个字符串拼接
        print(create_sql)
        cs1.execute(create_sql)


        # 提交
        conn.commit()

        # 3.关闭
        cs1.close()
        conn.close()


    def insert(self,**kwargs):
        """这个插入数据"""
        # 1.连接数据库
        # 创建connection连接
        conn = connect(host="localhost", port=3306, user="root", password="liweitao", charset="utf8", database="stock_db")
        cs1 = conn.cursor()


        # 通过字典生成我们的字段
        # insert_dict = {"uid":123,"name":"liweitao", 'email':"test@orm.org","password":"pwdpwd"}
        # 定义两个列表
        key_list = list()
        value_list = list()

        print(kwargs)

        for key,value in kwargs.items():
        # 添加到新的列表
            key_list.append(key)
        # 判断如果是int那么转成字符串
            if isinstance(value, int):
                value_list.append(str(value))
            else:
                value_list.append(""" '%s' """ % value) # 字符串中显示单引号
            # value_list.append(str(value))

        # 2.执行sql语句
        # insert_sql = """insert into user (uid, name, email, password) value (123,'liweitao', "test@orm.org", "pwd");"""
        insert_sql = """insert into %s (%s) value (%s);""" % (self.table_name, ",".join(key_list),",".join(value_list))
        print(insert_sql)
        cs1.execute(insert_sql)

        # 提交
        conn.commit()

        # 3.关闭
        cs1.close()
        conn.close()

        def select(self):
            conn = connect(host="localhost", user="root", password="liweitao", port=3306, database="stock_db",
                                   charset="utf8")
            cs1 = conn.cursor()
            select_sql = """select * from %s;""" % (self.table_name)
            cs1.execute(select_sql)
            data = cs1.fetchall()
            for temp in data:
                print(temp)
            cs1.close()
            conn.close()

        def delete(self, **kwargs):
            conn = connect(host="localhost", user="root", password="liweitao", port=3306, database="stock_db",
                                   charset="utf8")
            cs1 = conn.cursor()
            print(kwargs)
            for key, value in kwargs.items():
                delete_sql = """delete from %s where %s = '%s';""" % (self.table_name, key, value)
            print(delete_sql)
            cs1.execute(delete_sql)
            conn.commit()
            cs1.close()
            conn.close()

        def update(self, a, b, **kwargs):
            conn = connect(host="localhost", user="root", password="liweitao", port=3306, database="stock_db",
                                   charset="utf8")
            cs1 = conn.cursor()
            key_list = list()
            value_list = list()
            print(kwargs)
            for key, value in kwargs.items():
                key_list.append(key)
                update_sql = """update %s set %s = '%s' where %s = '%s' ;""" % (self.table_name, key, value, a, b)
                print(update_sql)
                cs1.execute(update_sql)
                conn.commit()
            cs1.close()
            conn.close()


class User(Createtable):
    # id = Fields("int unsigned primary key auto_increment not null")
    uid = Fields("int unsigned")
    name = Fields("varchar(30)")
    email = Fields("varchar(30)")
    password = Fields("Varchar(30)")




def main():
    """主入口"""
    # create()

    # insert()

    user = Caonidaba()
    user.create_table() # 用户表创建
    # user.insert(uid = 456, name = "yy") # 用户表插入


if __name__ == '__main__':
    main()
