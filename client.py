import socket


# 创建套接字
sockfd = socket.socket()

# 发起链接
sockfd.connect(('127.0.0.1', 8888))

# 收发消息
while True:
    string = input(">>")
    if not string:
        break
    sockfd.send(string.encode())
    data = sockfd.recv(1024)
    print("From server:", data.decode())

sockfd.close()
