import socket
import threading
import time


def send_msg(socket, addr):
    msg = input("请输入要发送的内容")
    socket.sendto(msg.encode("utf-8"), addr)
    time.sleep(5)


def recv_msg(socket):
    while True:
        print(threading.current_thread())
        msg, addr= socket.recvfrom(1024)
        print(msg.decode("utf-8"), addr)


def main():
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_server.bind(("", 8090))
    ip = input("请输入要发送消息的地址:")
    port = int(input("请输入要发送消息的端口:"))
    addr = (ip, port)
    while True:
        thread_recv = threading.Thread(target=recv_msg, args=(socket_server,))
        thread_recv.start()
        send_msg(socket_server, addr)
    socket.server.close()


if __name__ == '__main__':
    main()