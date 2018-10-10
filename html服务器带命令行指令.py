import gevent
import re
import socket
from gevent import monkey
import mini_web
import sys
monkey.patch_all()


class Service(object):
    def __init__(self,port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(("", port))
        self.socket.listen(128)

    def start(self):
        while True:
            client_socket, client_addr = self.socket.accept()
            print("连接成功", client_addr)
            gevent.spawn(self.run, client_socket)

    @staticmethod
    def run(client_socket):
            client_socket_recv = client_socket.recv(4096)
            msg = client_socket_recv.decode('utf-8')
            if msg:
                path = re.search('/.+? $', msg).group()
                print('地址为', path)
                open_path, state = mini_web.logic(path)
                try:
                    with open(open_path, 'rb') as f:
                        response_body = f
                except Exception as e:
                    print("异常", e)
                    return
                else:
                    response_line = "HTTP/1.1 %s" % state
                    response_head = "content-type:text/html;charset=utf8\r\n"
                    content = response_line.encode('utf-8') + response_head.encode('utf-8') +'\r\n'.encode('utf-8') +response_body
                    client_socket.send(content)
                finally:
                    client_socket.close()


def main():
    if len(sys.argv) != 2:
        print("启动命令为")
        return
    elif not sys.argv[1].isdigit:
        print("启动命令为")
        return
    port = int(sys.argv[1])
    service = Service(port)
    service.start()


if __name__ == '__main__':
    main()
