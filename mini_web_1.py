import re

from pymysql import connect

# 函数定义之后加上装饰器可以生成字典了

url_dict = dict()  # 空字典


# 这个flask最核心功能完成,路由功能

def set_url(url):
    def set_fun(func):
        def call_fun(*args, **kwargs):
            return func(*args, **kwargs)

        print(call_fun)

        # url_dict['/index.html'] = call_fun # 字典添加装饰后的函数引用

        url_dict[url] = call_fun  # 自动注册

        return call_fun

    return set_fun


def application(url):
    response_line = "HTTP/1.1 200 OK\r\n"

    response_head = "content-type:text/html;charset=utf-8\r\n"
    try:
        fun = url_dict[url]
        response_body = fun()


    except Exception as e:
        print("异常")
        response_line = "HTTP/1.1 404 NOT FOUND\r\n"
        response_body = "亲,您的界面已走失!"


    return response_line, response_head, response_body



########################################


# aop编程




@set_url("/index.html")
def index():
    with open("./templates/index.html") as f:
        content = f.read()

    # 一行的数据
    row_str = """<tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>
            <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000036">
        </td>
        </tr>"""
    # 从数据库查询出数据
    # 1. 从数据库得到数据
    # 1.1连接数据库
    # 创建Connection连接



    conn = connect(host='localhost', port=3306, database="stock_db", user="root", password="liweitao", charset="utf8")


    cs1 = conn.cursor()
    cs1.execute("select * from info;")
    data = cs1.fetchall()

    cs1.close()
    conn.close()

    table_str = ""
    for temp in data:
        table_str += row_str % (temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6], temp[7])


    # 替换内容
    new_content = re.sub(r"\{%content%\}",table_str,content)
    print(new_content)
    return new_content


@set_url("/center.html")
def center():
    with open("./templates/center.html") as f:
        content = f.read()
    conn = connect(host="localhost", user="root", password="liweitao", port=3306, database="stock_db", charset="utf8")
    cs1 = conn.cursor()
    cs1.execute("select info.code, info.short,info.chg,info.turnover,info.price,info.highs,focus.note_info from info inner join focus on info.id = focus.info_id;")
    data = cs1.fetchall()
    cs1.close()
    conn.close()
    row_str = """<tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <a type="button" class="btn btn-default btn-xs" href="/update/300268.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
            </td>
            <td>
                <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="300268">
            </td>
        </tr>
        """
    table_str = ""
    for temp in data:
        table_str += row_str % (temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6])

    new_table = re.sub(r"\{%content%\}", table_str, content)
    return new_table



