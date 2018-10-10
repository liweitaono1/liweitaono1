import gevent
import socket
import time
import route_table
from imp import reload
from gevent import monkey
monkey.patch_all()
reload(route_table)


class server(object):
    def __init__(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(("", 8080))
        server_socket.listen(128)
        self.socket= server_socket
        # self.client_socket = None
        # self.data = None

    def recve(self):
        client_socket, client_addr = self.socket.accept()
        data1 = client_socket.recv(1024)
        data = data1.decode("utf-8")
        print("发起请求", client_addr)
        # self.client_socket = client_socket
        # self.data = data
        return client_socket, data

    def response(self):
        client_socket, data = self.recve()

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
            client_socket.send(content)

    def __str__(self):
        pass

    def __call__(self):
        while True:
            self.recve()
            self.response()

ser = server()
ser()




















