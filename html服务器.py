import socket
import re


def response_msg(state, path=None):
    length = len(path)
    response_head = "HTTP/1.1 %s" % state
    response_hang = "Content_Length: %d\r\nContent_Type: text/html;charset=utf-8\r\n" % length
    response_body = path
    content = response_head + "\r\n" + response_hang + "\r\n" + response_body
    return content


def send(client_socket, data):
    client_socket.send(data.encode("utf-8"))

# GET /index.html HTTP/1.1
# HOST: localhost:127.0.0.1

def main():
    SERVICE_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVICE_SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    SERVICE_SOCKET.bind(("", 9090))
    SERVICE_SOCKET.listen(128)
    while True:
        client_socket, client_addr = SERVICE_SOCKET.accept()
        data = client_socket.recv(4096)
        if data:
            msg = data.decode("utf-8")
            list = re.findall("GET (/.+?) HTTP/1\.1", msg)
            print(list)
            if list[0] == "/index.html":
                data = response_msg("200 OK", "/index.html/")
                send(client_socket, data)

            elif list[0] == "/center.html":
                data = response_msg("200 OK", "/centet.html/")
                send(client_socket, data)

            elif list[0] == "/login.html":
                data = response_msg("200 OK", "/login.html/",)
                send(client_socket, data)

            else:
                data = response_msg("404 NOTFOUND", "1")
                send(client_socket, data)

        else:
            client_socket.close()
            print("断开连接")
            break


if __name__ == '__main__':
    main()


