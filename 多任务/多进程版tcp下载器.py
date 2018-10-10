import os
import time
import multiprocessing
import socket


def set_fun(founc):
    def call_fun(*args, **kwargs):
        founc(*args, **kwargs)
        print(multiprocessing.current_process().pid)
    return call_fun


@set_fun
def download(client_socket):
    try:
        print("子", multiprocessing.current_process().pid)
        data = client_socket.recv(1024)
        file_name = data.decode("utf-8")
        if os.path.exists(file_name):
            print(file_name)
            with open(file_name, "rb") as f:
                while True:
                    send_data = f.read(1024)
                    if send_data:
                        client_socket.send(send_data)
                    else:
                        time.sleep(10)
                        client_socket.close()
                        print("下载完成")
                        break
        else:
            print("文件不存在")
    except Exception as e:
        print(e)
    finally:
        client_socket.close()
        print("断开连接1")



def main():
    print("主",multiprocessing.current_process().pid)
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_server.bind(("", 8080))
    socket_server.listen(128)
    # pool = multiprocessing.Pool(4)
    while True:
        client_socket, client_addr = socket_server.accept()
        print("请求下载", client_addr)
        m = multiprocessing.Process(target=download, args=(client_socket,))
        m.start()
        # pool.apply_async(download(client_socket))
        print("断开连接")
        # download(client_socket)

    # pool.join()
    # pool.close()
    socket_server.close()


if __name__ == '__main__':
    main()





