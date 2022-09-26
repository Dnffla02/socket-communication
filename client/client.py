import socket

IP = 'localhost'
T_PORT = 10000
U_PORT = 10001
BUFFER = 1024

while(1):
    print('--------------------------------------------------')
    msg = input('계산할 수학식:')
    communication = input("통신할 네트워크 유형 [TCP/UDP]: ").lower()
    if communication == 'tcp':
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.connect((IP, T_PORT))
            server.sendall(msg.encode(encoding='utf-8'))
            print('결과:', server.recv(BUFFER).decode())
            server.close()
        except Exception as e:
            print('[ERROR]', e)
    elif communication == 'udp':
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            server.sendto(msg.encode(encoding='utf-8'), (IP, U_PORT))
            result, server = server.recvfrom(BUFFER)
            print('결과:', result.decode())
        except Exception as e:
            print('[ERROR]', e)
    else:
        print("잘못된 유형입니다.")
