import gevent
from gevent import monkey
import time
import socket
import re
monkey.patch_all()
# gevent.monkey.patch_all()


def response(socket_client):
    recv_msg = socket_client.recv(1024)
    request = recv_msg.decode("utf-8")
    print(request)
    # re_request = re.match(r".+? ", request).group()
    # print(re_request)
    # if re_request == "GET":
    response_line = "HTTP/1.1 200 OK\r\n"
    response_body = "茶大赛的:XXXXXXXXXXXX"
    # length = len(response_body)
    response_head = "content-type:text/html;charset=utf-8\r\n"
    content = response_line + response_head + "\r\n" + response_body
    socket_client.send(content.encode("utf-8"))





def main():
    """
    编写协程版 HTTP服务器，实现功能：
    客户端接入，返回客户端IP地址及商品 然后关闭客户端
    """
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_server.bind(("", 8081))
    socket_server.listen(128)
    join_list = []
    while True:
        socket_client, socket_addr = socket_server.accept()
        gevent_join = gevent.spawn(response(socket_client))
        join_list.append(gevent_join)
    gevent.joinall(join_list)



if __name__ == '__main__':
    main()










