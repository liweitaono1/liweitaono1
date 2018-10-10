import socket


def main():
    request_head = "GET /index.html HTTP/1.1\r\n"
    request_hang = "HOST: localhost:127.0.0.1\r\n"
    content = request_head + request_hang + "\r\n你好"
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    client_socket.bind(("", 8081))
    client_socket.connect(("127.0.0.1", 9090))
    # print(content)
    client_socket.send(content.encode("utf-8"))
    response_data = client_socket.recv(4096)
    msg = response_data.decode("utf-8")
    # print(msg)



if __name__ == '__main__':
    main()
