import socket
import time

LISTEN_IP = '0.0.0.0'
LISTEN_PORT = 5005
RECEIVED_LOG = []

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((LISTEN_IP, LISTEN_PORT))

print(f"포트 {LISTEN_PORT}에서 수신 대기 중...")

try:
    while True:
        data, addr = sock.recvfrom(1024)
        recv_time = time.time()
        decoded = data.decode()
        parts = decoded.split(',')
        if len(parts) >= 2:
            seq_num = int(parts[0])
            send_time = float(parts[1])
            delay = abs(recv_time - send_time)
            RECEIVED_LOG.append((seq_num, send_time, recv_time, delay))
            print(f"[#{seq_num}] 지연 시간: {delay*1000:.2f} ms")
        else:
            print(f"⚠️ 잘못된 메시지 포맷: {decoded}")
except KeyboardInterrupt:
    # 로그 저장
    with open("udp_recv_log.csv", "w") as f:
        for log in RECEIVED_LOG:
            f.write(','.join(map(str, log)) + '\n')
    print("수신 종료. udp_recv_log.csv 저장 완료.")