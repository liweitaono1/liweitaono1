import socket
import threading
import os
import time


def set_foun(founc):
    def call_foun(socket_server, file, server_addr):
        start_time = time.time()
        a = founc(socket_server, file, server_addr)
        time.sleep(5)
        end_time = time.time()
        run_time = end_time - start_time
        print(run_time)
        return a
    return  call_foun


@set_foun
def download(socket_server, file, server_addr):
    print(threading.current_thread())
    if os.path.exists(file):
        print("请求下载", server_addr)
        with open(file, "rb") as f:
            while True:
                file_data = f.read(1024)
                if file_data:
                    socket_server.sendto(file_data, server_addr)
                else:
                    print("下载完成")
                    break
    else:
        print("文件不存在")


def main():
    while True:
        socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        socket_server.bind(("127.0.0.1", 8080))
        while True:
            server_data, server_addr = socket_server.recvfrom(1024)
            file = server_data.decode("utf-8")
            t = threading.Thread(target=download, args=(socket_server, file, server_addr))
            t.start()
    socket_server.close()

if __name__ == '__main__':
    main()
    
    