import socket


def main():
    try:
        host = ""
        port = 4444
        s = socket.socket()
    except socket.error as msg:
        print("소켓 생성 에러: " + str(msg))
        return 0
    
    try:
        print(f"소켓을 {port}번 포트에 바인딩 중 입니다...", )
        s.bind((host, port))
        s.listen(1)
    except:
        print("소켓 바인딩 에러: " + str(msg))
        return 0

    conn, address = s.accept()
    print(f"연결되었습니다!(IP: {address[0]}, PORT: {address[1]}\n")

    while True:
        cmd = input()
        
        if cmd == "quit":
            conn.close()
            s.close()
            return 0

        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_reponse = str(conn.recv(1048576) , "utf-8")
            print(client_reponse, end="")

    conn.close()


main()