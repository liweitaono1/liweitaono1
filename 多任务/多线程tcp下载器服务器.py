
import os
import socket
# import threading
import time
import multiprocessing


# def download(client_socket):
#     data = client_socket.recv(1024)
#     file_name = data.decode("utf-8")
#     if os.path.exists(file_name):
#         f = open(file_name, "rb")
#         while True:
#             content = f.read(10240)
#             if content:
#                 client_socket.send(content)
#             else:
#                 print("下载完成")
#                 client_socket.close()
#                 print(1)
#                 f.close()
#                 break
#     else:
#         print("文件不存在")

def recv(client):
    while True:
        msg = client.recv(1024)
        if msg:
            print(msg.decode())
        else:
            break

def main():
    severse_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    severse_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    severse_socket.bind(("", 8082))
    severse_socket.listen(128)
    while True:
        client_socket, client_addr = severse_socket.accept()
        print("请求下载",client_addr)
        # download_thread = threading.Thread(target=download, args=(client_socket,))
        # download_thread.setDaemon(True)
        # download_thread.start()
        multiprocessing.Process(target= recv, args=(client_socket,)).start()

    severse_socket.close()


if __name__ == '__main__':
    main()

