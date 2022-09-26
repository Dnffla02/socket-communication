import socket

IP = 'localhost'
PORT = 10001
BUFFER = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((IP, PORT))



print('UDP 메인 서버 실행')
try:
    while(1):

        data, addr = server.recvfrom(BUFFER)
        print('--------------------------------------------------')
        print('연결된 클라이언트:', addr)
        msg = data.decode()
        print('받은 메세지: [', msg,']')
        if '+' in msg or '-' in msg:
            print('[ 10010포트 연결 ]')
            PMSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            PMSocket.connect((IP, 10010))
            PMSocket.sendall(data)
            server.sendto(PMSocket.recv(BUFFER), addr)
            PMSocket.close()
        elif '*' in msg or '/' in msg:
            print('[ 10011포트 연결 ]')
            MDSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            MDSocket.connect((IP, 10011))
            MDSocket.sendall(data)
            server.sendto(MDSocket.recv(BUFFER), addr)
            MDSocket.close()
        else:
            socket.sendall("ERROR".encode(encoding='utf-8'))
except Exception as e:
    print ('ERROR_',e)
finally:
    server.close()
