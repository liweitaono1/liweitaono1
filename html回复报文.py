import socket

if __name__ == '__main__':
    # 创建tcp客户端套接字
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接
    tcp_client_socket.connect(("tlias3.boxuegu.com", 80))
    # 请求行
    request_line = "GET / HTTP/1.1\r\n"
    # 请求头
    request_header = "Host: tlias3.boxuegu.com\r\nConnection:close\r\n"
    # 准备http请求报文数据
    request_content = request_line + request_header + "\r\n"
    # 发送http请求报文数据
    tcp_client_socket.send(request_content.encode("utf-8"))
    # 定义二进制响应数据的类型
    result = b""
    # 接收服务端http响应报文数据
    while True:
        # 提示： 服务端断开连接，recv会解阻塞，返回的数据长度0
        # 提示： 以后可以通过Content-Length判断服务端发送数据的长度
        recv_data = tcp_client_socket.recv(1024)
        if recv_data:
            # 表示接收到了数据
            result += recv_data

            # print(result)
        else:
            break

    # 显示原始的响应报文数据
    print(result)
    # 解码 ： 把二进制数据转成字符串
    response_content = result.decode("utf-8")
    # 根据指定标识数据进行分割
    response_list = response_content.split("\r\n\r\n", 1)
    # response_content.split("\r\n\r\n", maxsplit=1)

    print(len(response_list))
    print(response_list[1])
    # 关闭套接字
    tcp_client_socket.close()

