# coding=utf-8
import socket


def client():
    n = 4
    win_start = 0
    win_end = 2
    host = socket.gethostname()
    port = 12344

    client_socket = socket.socket()
    client_socket.connect((host, port))

    print('bye를 입력하면 종료합니다')
    message = input("Enter를 입력해 Frame 전송 --> ")

    while message.lower().strip() != 'bye':
        print("Frame 전송...")
        for i in range(n):
            print("Frame -> ", win_start + i)

        msg = str(win_start)
        client_socket.send(msg.encode())
        data = client_socket.recv(1024).decode()
        msg = str(data)
        win_start = int(msg)
        win_end = win_start + n - 1

        print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
        print('수신된 ACK server: ' + data)

        message = input("아무 문자를 입력해 Frame 전송 --> ")

    client_socket.close()


if __name__ == '__main__':
    client()
