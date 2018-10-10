import socket


def tcp_socket(tcp_port, mode='tcp', udp_connect_ip = None, udp_connect_port = None):
    if mode == 'tcp':
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # print(tcp_port)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(("", tcp_port))
        server.listen(128)
        while True:
            tcp_client_socket, tcp_cliet_addr = server.accept()
            return tcp_client_socket, tcp_cliet_addr
        server.close()
    elif mode == 'udp':
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.connect((udp_connect_ip,udp_connect_port))


