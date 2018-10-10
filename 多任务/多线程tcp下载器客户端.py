import socket

def send_name(client_socket):
    file_name = input("请输入文件名:")
    client_socket.send(file_name.encode("utf-8"))

def download(client_socket):
    with open("new.png", "ab") as f:
        while True:
            data = client_socket.recv(10240)
            if data:
                f.write(data)
            else:
                break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 8082))
    send_name(client_socket)
    download(client_socket)
    client_socket.close()

if __name__ == '__main__':
    main()
# import socket
#
# if __name__ == '__main__':
#     # 创建tcp客户端socket
#     tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # 建立连接
#     tcp_client_socket.connect(("127.0.0.1",8082 ))
#     # 获取用户输入文件名
#     file_name = input("请输入您要下载的文件名:")
#     # 使用gbk进行编码
#     file_name_data = file_name.encode("gbk")
#     # 代码执行到此，说明连接建立成功
#     tcp_client_socket.send(file_name_data)
#     with open("new" + file_name, "wb") as file:
#         # 循环接收服务端发送的文件二进制数据
#         while True:
#             # 获取服务端文件数据
#             file_data = tcp_client_socket.recv(1024)
#             if file_data:
#                 # 写入到指定文件
#                 file.write(file_data)
#             else:
#                 break
#
#     # 关闭socket
#     tcp_client_socket.close()