import gevent
import socket
import time
import route_table
from imp import reload
from gevent import monkey
monkey.patch_all()
reload(route_table)


def response(socket):
    print(gevent.getcurrent())
    data = socket.recv(1024)
    path, state = route_table.search_path(data)
    try:
        with open(path, "rb") as f:
            response_body = f.read()
    except Exception as e:
        print(e)
        response_head = "content-type:text/html;charset=utf-8\r\n"
        response_line = "HTTP/1.1 %s\r\n" % state
        content = response_line.encode("utf-8") + response_head.encode("utf-8") + "\r\n".encode("utf-8")
    else:
        response_head = "content-type:text/html;charset=utf-8\r\n"
        response_line = "HTTP/1.1 %s\r\n" % state
        content = response_line.encode("utf-8") + response_head.encode("utf-8") + "\r\n".encode("utf-8") + response_body
    finally:
        time.sleep(5)
        socket.send(content)


def main():
    """
    1.默认请求（ / ）时，   “hello python , 您请求的页面跳转为 index.html”
    2.请求 index.html  时，返回 1 中的内容
    3.请求 aa.html 时，返回 404 错误
    要求：使用标准响应报文返回数据。
    """
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_server.bind(("", 8080))
    socket_server.listen(128)
    join_list = []
    while True:
        client_socket, client_addr = socket_server.accept()
        g = gevent.spawn(response(client_socket))
        join_list.append(g)

    gevent.joinall(join_list)


if __name__ == '__main__':
    main()