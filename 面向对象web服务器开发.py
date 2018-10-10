import re
import gevent
import socket
from gevent import monkey
import mini_web
monkey.patch_all()


class Service(object):
    def __init__(self):
        socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        socket1.bind(("", 8080))
        socket1.listen(128)
        self.socket = socket1

    def start(self):
        while True:
            client_socket, client_addr = self.socket.accept()
            gevent.spawn(self.run, client_socket)

    @staticmethod
    def run(client_socket):
        data = client_socket.recv(4096)
        print("连接成功")
        msg = data.decode("utf-8")
        path = re.search(r"GET (.*?) HTTP/1.1", msg)
        print(msg)
        if path:
            open_path, state = mini_web.logic(path.group(1))
            try:
                with open("./"+open_path, "rb") as f:
                    content = f.read()
            except Exception as e:
                print("异常为:", e)
                client_socket.send(("HTTP/1.1 %s\r\n" % state).encode("utf-8"))
            else:
                response_line = "HTTP/1.1 %s\r\n" % state
                response_head = "content-type:text/html;charset=utf8\r\n"
                response_body = content
                response_msg = response_line.encode("utf-8") + response_head.encode("utf-8") + '\r\n'.encode("utf-8") + response_body
                client_socket.send(response_msg)
            finally:
                client_socket.close()
                print("断开连接")
        else:
            client_socket.close()
            print("断开连接")
            return


def main():
    sevice =Service()
    sevice.start()


if __name__ == '__main__':
    main()



