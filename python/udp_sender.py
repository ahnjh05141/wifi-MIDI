import socket
import time

DEST_IP = '127.0.0.1'  # 수신자 IP
DEST_PORT = 5005
MESSAGE_COUNT = 1000
INTERVAL = 0.001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(MESSAGE_COUNT):
    timestamp = time.time()
    message = f"{i},{timestamp}".encode()
    sock.sendto(message, (DEST_IP, DEST_PORT))
    time.sleep(INTERVAL)

print(f"총 {MESSAGE_COUNT}개의 메시지를 전송했습니다.")