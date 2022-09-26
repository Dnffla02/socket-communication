import socket

IP = 'localhost'
PORT = 10011
BUFFER = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((IP, PORT))
server.listen()
print('곱셈/나눗셈 전용 서버 실행')

try:
    while(1):
        mainServer, addr = server.accept()
        print('--------------------------------------------------')
        print('연결된 메인 서버:', addr)
        data = mainServer.recv(BUFFER).decode()
        print('받은 메세지: [', data,']')
        if '*' in data:
            msgs = data.split('*')
            result = int(msgs[0])*int(msgs[1])
            print('결과: [ '+str(result)+' ]')
            mainServer.sendall(str(result).encode(encoding='utf-8'))
        elif '/' in data:
            msgs = data.split('/')
            result = int(msgs[0])/int(msgs[1])
            print('결과: [ '+str(result)+' ]')
            mainServer.sendall(str(result).encode(encoding='utf-8'))
except Exception as e:
    print ('ERROR_',e)
finally:
    server.close()