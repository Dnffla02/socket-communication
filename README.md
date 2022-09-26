# socket-communication
socket com

소켓 통신 구조
server:
 sub:
  pm.py - 합, 차를 계산해주는 서버
  md.py - 곱셉, 나눗셈을 계산해주는 서버
 main:
  tcp.py - tcp만을 전용으로 받는 서버
  udp.py - udp만을 전용으로 받는 서버
client:
 client.py - tcp, udp 서버를 선택해 계산식을 보냄
 
예시
 1+2<enter>
 tcp
 ----------
 3
  
과제용으로 쓰는 경우에는
눈치껏 바꿔서 냅시다~
