import socket

IP = 'localhost'
PORT = 10000
BUFFER = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((IP, PORT))
server.listen()

print('TCP 메인 서버 실행')
try:
    while(1):
        client, addr = server.accept()
        print('--------------------------------------------------')
        print('연결된 클라이언트:', addr)
        data = client.recv(BUFFER)
        msg = data.decode()
        print('받은 메세지: [', msg,']')
        if '+' in msg or '-' in msg:
            print('[ 10010포트 연결 ]')
            PMSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            PMSocket.connect((IP, 10010))
            PMSocket.sendall(data)
            client.sendall(PMSocket.recv(BUFFER))
            PMSocket.close()
        elif '*' in msg or '/' in msg:
            print('[ 10011포트 연결 ]')
            MDSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            MDSocket.connect((IP, 10011))
            MDSocket.sendall(data)
            client.sendall(MDSocket.recv(BUFFER))
            MDSocket.close()
        else:
            socket.sendall("ERROR".encode(encoding='utf-8'))
except Exception as e:
    print ('ERROR_',e)
finally:
    server.close()



    #message, clientAddress = socket.recv_fds(2048)
        #serverSocket.sendto(message.encode(), clientAddress)