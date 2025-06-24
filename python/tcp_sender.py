import socket
import time

DEST_IP = '127.0.0.1'  # 서버 주소
DEST_PORT = 5005
MESSAGE_COUNT = 10000
INTERVAL = 0.01

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((DEST_IP, DEST_PORT))

for i in range(MESSAGE_COUNT):
    timestamp = time.time()
    message = f"{i},{timestamp}".encode()
    sock.sendall(message)
    time.sleep(INTERVAL)

sock.close()
print(f"총 {MESSAGE_COUNT}개의 메시지를 전송했습니다.")