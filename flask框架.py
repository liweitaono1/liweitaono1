# 初始化tcp服务器端
# 循环接收用户(浏览器)请求
# 处理用户请求
# 1. 根据不同的请求地址返回不同的数据
# 关闭

# 一个函数一个功能
# 类是相关函数的集合,或者封装
import socket
import mini_web_1
import gevent
from gevent import monkey
monkey.patch_all()
import re


class Server(object):
    def server_exec(self, client_socket):
        data = client_socket.recv(1024).decode("utf-8")
        print(data)
        url = re.search(r"GET\s(/.*?)\s", data).group(1)
        print(url)
        if url:
            if url == "/":
                url = "/index.html"
        else:
            client_socket.close()
        if url.endswith(".html"):
            response_line, response_head, response_body = mini_web_1.application(url)
            response_content = response_line + response_head + "\r\n" + response_body
            client_socket.send(response_content.encode("utf-8"))
        else:
            try:
                response_line = "HTTP/1.1 200 OK\r\n"
                response_head = "content-type:text/html;charset=utf8"

                with open("./static%s" % url, "rb") as f:
                    content = f.read()
                    response_content = response_line + response_head + "\r\n"
                    client_socket.send(response_content.encode("utf-8"))
                    client_socket.send(content)
            except Exception as e:
                response_line = "HTTP/1.1 404 NOT FOUND\r\n"
                response_head = "content-type:text/html;charset=utf8"
                response_body = ""
                response_content = response_line + response_head + "\r\n" + response_body
                client_socket.send(response_content.encode("utf-8"))
        client_socket.close()


    def run(self):
        while True:
            client_socket, client_addr = self.tcp_socket.accept()
            gevent.spawn(self.server_exec, client_socket)
        self.tcp_socket.close

    def __init__(self):
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcp_socket.bind(("", 8080))
        self.tcp_socket.listen(128)


def main():
    server = Server()
    server.run()


if __name__ == '__main__':
    main()
