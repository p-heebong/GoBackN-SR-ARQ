# coding=utf-8
import socket
import random


def server():

    host = socket.gethostname()
    port = 12344
    exp = 0
    n = 4
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("연결된 Client: ", str(address))

    while True:

        data = conn.recv(1024).decode()
        if not data:
            break

        rec = int(data)
        count = 0
        flag = 0
        lim = rec + n - 1

        while count != n:
            recFrame = random.randint(rec, lim)
            print("들어오는 Frame -> ", recFrame, "    기다리는 Frame -> ", exp)
            if recFrame != exp:
                print("버린 Frame  -> ", recFrame)
                flag = 1
                break
            else:
                print("받은 Frame -> ", recFrame)
                count += 1
                exp += 1
                rec += 1
                continue

        if flag == 1:
            ack = exp
        else:
            ack = str(int(data) + n)

        print("전송한 ACK    -> ", ack)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
        data = str(ack)
        conn.send(data.encode())

    conn.close()


if __name__ == '__main__':
    server()