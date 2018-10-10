import socket
import multiprocessing
import time
import threading
import gevent
from gevent import monkey
monkey.patch_all()


def recv_msg(socket_client):
    while True:
        data = socket_client.recv(1024)
        msg = data.decode("utf-8")
        print(msg)
    socket_client.close()


def main():
    socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_tcp.bind(("", 8080))
    socket_tcp.listen(128)
    # pool = multiprocessing.Pool(3)
    while True:
        socket_client, socket_addr = socket_tcp.accept()
        msg = input("请输入要发送的消息")
        socket_client.send(msg.encode("utf-8"))
        # gevent.spawn(recv_msg(socket_client))
        # pool.apply_async(recv_msg(socket_client))
        th = threading.Thread(target=recv_msg, args=(socket_client,))
        th.start()
    # pool.close()
    # pool.join()


if __name__ == '__main__':
    main()
