import socket



def main():
    # ip = input("请输入地址")
    # port = int(input("请输入端口"))
    # files = input("请输入要下载的文件")
    # file = files.encode("utf-8")
    # addr = (ip, port)
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_client.bind(("", 8090))
    socket_client.connect(("127.0.0.1", 8080))
    socket_client.send(" 2.jpeg".encode("utf-8"))
    path = "22.jpeg"
    print(path)
    with open(path, "wb") as f:
        while True:
            data = socket_client.recv(1024)
            if data:
                f.write(data)
            else:
                socket_client.close()
                print(1)
                break


if __name__ == '__main__':
    main()
