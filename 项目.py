import re
import pymysql
import time

"""
# 装饰器传参
三个函数的嵌套, 第三层函数内包含一个闭包, 第三层返回一个闭包的引用, 第三层参数必须有参数


def set_args(args):
    def set_func(func):
        def call_func(*args, **kwargs):
            return func()

        return call_func

    return set_func


@set_args("参数")
def test():
    print("test")


作用: 可以用来传参数
"""
value = 0


def set_fun(func):
    # value = 0
    def call_fun(*args, **kwargs):
        # nonlocal value
        global value
        func(*args, **kwargs)
        value += 1
        # print(value)
        return func(*args, **kwargs)
    return call_fun


def set_fun_t(func):
    def call_fun():
        start_time = time.time()
        func(start_time)
        end_time = time.time()
        run_time = end_time - start_time
        print("运行了", int(run_time))
    return call_fun


@set_fun
def register():  # 添加账号,添加权限
    while True:
        data = input("请输入用户名:'由字母,数字,下划线组成,6-8位组成'")
        name = re.match("\w{6,8}", data).group()
        print("用户名为%s" % name)
        ensure = input("是否使用当前用户名[1]使用[2]退出")
        if ensure == "1":
            password = input("请输入密码:由字母,数字,下划线组成,6-8位组成")
            password_re = re.match("\w{6,8}", password).group()
            password1 = input("请确认密码:")
            password_re1 = re.match("\w{6,8}", password1).group()
            if password_re == password_re1:
                conn = pymysql.connect(host="localhost", user="root", password="liweitao", port=3306, charset="utf8")
                cur = conn.cursor()
                sql = """create user '%s'@'localhost' identified by '%s';""" % (name, password_re)
                cur.execute(sql)
                conn.commit()
                sql1 = """grant all privileges on class.* to '%s'@'localhost';""" % name
                cur.execute(sql1)
                conn.commit()
                cur.close()
                conn.close()
        elif ensure == "2":
            break


@set_fun
def login():  # 登录
    while True:
        try:
            name = input("请输入用户名:")
            name1 = re.match("\w{4,8}", name).group()
            password = input("请输入密码:")
            password1 = re.match("\w{4,8}", password).group()
            conn = pymysql.connect(host="localhost", user=name1, password=password1, port=3306, database='class', charset='utf8')
        except Exception as e:
            print("请重新输入,错误:", e)
        else:
            print("登录成功")
            conn.close()
            return name1, password1


@set_fun
def addition(conn, cur):
    try:
        student_name = input("请输入要添加学生的名字")
        student_age = int(input("请输入要添加学生的年龄"))
        student_id = int(input("请输入要添加学生的学号"))
        student_gender = input("请输入要添加学生的性别")
        student_height = int(input("请输入要添加学生的身高"))
        student_class_id = int(input("请输入要添加学生的班级"))
        sql = """insert into student values(0,'%s',%d,%d,'%s',%d,%d)""" % (student_name, student_age, student_id, student_gender, student_height, student_class_id)
        cur.execute(sql)
        print(student_name, student_age, student_id, student_gender, student_height, student_class_id)
    except Exception as e:
        print(e)
    else:
        c = input("确认修改请按[1]取消[2]")
        if c == "1":
            conn.commit()
        else:
            conn.rollback()


@set_fun
def dele(conn, cur):
    try:
        student_name = input("请输入要删除学生的姓名")
        sql = """delete from student where name='%s';""" % student_name
        cur.execute(sql)
    except Exception as e:
        print(e)
    else:
        c = input("确认修改请按[1]取消[2]")
        if c == "1":
            conn.commit()
        else:
            conn.rollback()


@set_fun
def update(conn, cur):
    try:
        command = input("请输入要修改的内容[1]姓名[2]年龄[3]学号[4]性别[5]身高[6]班级")
        if command == "1":
            student = input("请输入要修改的学生")
            student_name = input("修改-")
            sql = """update student set name = '%s' where name = '%s';""" % (student_name, student)
            cur.execute(sql)
            c = input("确认修改请按[1]取消[2]")
            if c == "1":
                conn.commit()
            else:
                conn.rollback()
        if command == "2":
            student = input("请输入要修改的学生")
            student_age = input("修改-")
            sql = """update student set age = %d where name = '%s';""" % (student_age, student)
            cur.execute(sql)
            c = input("确认修改请按[1]取消[2]")
            if c == "1":
                conn.commit()
            else:
                conn.rollback()
        if command == "3":
            student = input("请输入要修改的学生")
            student_id = input("修改-")
            sql = """update student set student_id = %d where name = '%s';""" % (student_id, student)
            cur.execute(sql)
            c = input("确认修改请按[1]取消[2]")
            if c == "1":
                conn.commit()
            else:
                conn.rollback()
        if command == "4":
            student = input("请输入要修改的学生")
            student_gender = input("修改-")
            sql = """update student set gender = '%s' where name = '%s';""" % (student_gender, student)
            cur.execute(sql)
            c = input("确认修改请按[1]取消[2]")
            if c == "1":
                conn.commit()
            else:
                conn.rollback()
        if command == "5":
            student = input("请输入要修改的学生")
            student_height = input("修改-")
            sql = """update student set height = %d where name = '%s';""" % (student_height, student)
            cur.execute(sql)
            c = input("确认修改请按[1]取消[2]")
            if c == "1":
                conn.commit()
            else:
                conn.rollback()
        if command == "6":
            student = input("请输入要修改的学生")
            student_class_id = input("修改-")
            sql = """update student set class_id = %s where name = %s;"""
            print(sql)
            cur.execute(sql, (student_class_id, student))
            c = input("确认修改请按[1]取消[2]")
            if c == "1":
                conn.commit()
            else:
                conn.rollback()
    except Exception as e:
        print(e)


@set_fun
def select(cur):
    try:
        student = input("请输入要查询学生的姓名")
        sql = """select * from student where name = '%s';""" % student
        cur.execute(sql)
        print(cur.fetchone())
    except Exception as e:
        print(e)


@set_fun
def addition_class(conn, cur):
    try:
        name = input("请输入要添加班级的名字")
        class_id = int(input("请输入要添加班级号"))
        instruct = input("请添加班主任姓名")
        sql = """insert into class values(0,'%s',%d,'%s')""" % (name, class_id, instruct)
        cur.execute(sql)
        print(name, class_id, instruct)
    except Exception as e:
        print(e)
    else:
        c = input("确认修改请按[1]取消[2]")
        if c == "1":
            conn.commit()
        else:
            conn.rollback()


@set_fun
def dele_class(conn, cur):
    try:
        class_name = input("请输入要删除班级的名称")
        sql = """delete from class where name='%s';""" % class_name
        cur.execute(sql)
    except Exception as e:
        print(e)
    else:
        c = input("确认修改请按[1]取消[2]")
        if c == "1":
            conn.commit()
        else:
            conn.rollback()


@set_fun
def update_class(conn, cur):
    try:
        command = input("请输入要修改的内容[1]名称[2]班级号[3]班主任")
        if command == "1":
            class_name = input("请输入要修改班级的名称")
            name = input("修改-")
            sql = """update class set name = '%s' where name = '%s';""" % (name, class_name)
            cur.execute(sql)
            c = input("确认修改请按[1]取消[2]")
            if c == "1":
                conn.commit()
            else:
                conn.rollback()
        if command == "2":
            class_name = input("请输入要修改的班级的名称")
            class_id = int(input("修改-"))
            sql = """update class set class_id = %d where name = '%s';""" % (class_id, class_name)
            cur.execute(sql)
            c = input("确认修改请按[1]取消[2]")
            if c == "1":
                conn.commit()
            else:
                conn.rollback()
        if command == "3":
            class_name = input("请输入要修改的班级的名称")
            instruct = input("修改-")
            sql = """update class set instruct = '%s' where name = '%s';""" % (instruct, class_name)
            cur.execute(sql)
            c = input("确认修改请按[1]取消[2]")
            if c == "1":
                conn.commit()
            else:
                conn.rollback()

    except Exception as e:
        print(e)


@set_fun
def select_class(cur):
    try:
        class_name = input("请输入要查询班级的名称")
        sql = """select * from class where name = '%s';""" % class_name
        cur.execute(sql)
        print(cur.fetchone())
    except Exception as e:
        print(e)


@set_fun
def selectall(cur):
    sql = """select * from student;"""
    cur.execute(sql)
    msg = cur.fetchall()
    for x in msg:
        print(x)


@set_fun
def selectall_class(cur):
    sql = """select * fro class;"""
    cur.execute(sql)
    msg = cur.fetchall()
    for x in msg:
        print(x)


@set_fun_t
def main(start_time):
    """
    学生管理系统:
    一个注册,
    一个登陆,
    增删改查
    班级管理
    班号班名班主任
    学号姓名年龄性别身高班
    """
    # while True:
    #     command = input("[1]注册[2]登录")
    #     if command == "1":
    #         register()
    #
    #     elif command == "2":
    #         login()
    #         user, password = login()
    #         break
    #
    #     else:
    #         print("输入错误")
    conn = pymysql.connect(host="localhost", user="root", password="liweitao", port=3306, database='class', charset='utf8')
    cur = conn.cursor()
    while True:
        command = input("注册[1]登录[2]退出[3]")
        if command == "1":
            try:
                user_name = input("请输入用户名")
                user_password = input("请输入密码")
                sql = """insert into user values(0, '%s', '%s');""" % (user_name, user_password)
                cur.execute(sql)
            except Exception as e:
                print(e)
            else:
                print("账号:%s, 密码:%s" % (user_name, user_password))
                c = input("确认修改请按[1]取消[2]")
                if c == "1":
                    conn.commit()
                else:
                    conn.rollback()

        elif command == "2":
            user_name = input("请输入用户名")
            user_password = input("请输入密码")
            sql = """select user,password from user where user = '%s';""" % user_name
            cur.execute(sql)
            account = cur.fetchone()
            if account[1] == user_password:
                while True:
                    command1 = input("[1]管理学生[2]管理班级[3]显示操作次数[4]显示操作时间[5]返回上一级")
                    if command1 == "1":     # 学生管理
                        while True:
                            command2 = input("[1]增[2]删[3]改[4]查[5]查看所有人信息[6]返回上一级")
                            if command2 == "1":
                                addition(conn, cur)

                            elif command2 == "2":
                                dele(conn, cur)

                            elif command2 == "3":
                                update(conn, cur)

                            elif command2 == "4":
                                select(cur)

                            elif command2 == "5":
                                selectall(cur)

                            elif command2 == "6":
                                print("返回上一级")
                                break

                            else:
                                print("输入错误,请重新输入")

                    elif command1 == "2":  # 班级管理
                        while True:
                            command3 = input("[1]增[2]删[3]改[4]查[5]查看所有班级信息[6]返回上一级")
                            if command3 == "1":
                                addition_class(conn, cur)

                            elif command3 == "2":
                                dele_class(conn, cur)

                            elif command3 == "3":
                                update_class(conn, cur)

                            elif command3 == "4":
                                select_class(cur)

                            elif command3 == "5":
                                selectall_class(cur)

                            elif command3 == "6":
                                print("返回上一级")
                                break

                            else:
                                print("输入错误,请重新输入")

                    elif command1 == "3":
                        print("操作次数:", value)

                    elif command1 == "4":
                        current_time = time.time()
                        running_time = current_time - start_time
                        print("操作时间:", int(running_time))

                    elif command1 == "5":
                        print("返回上一级")
                        break

                    else:
                        print("输入错误,请重新输入")

            else:
                print("账号或密码错误")

        elif command == "3":
                cur.close()
                conn.close()
                break

        else:
            print("输入错误")


if __name__ == '__main__':
    main()
