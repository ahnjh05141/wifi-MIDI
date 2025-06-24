import socket
import time

RECEIVED_LOG = []
HOST = '0.0.0.0'
PORT = 5005

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"TCP 수신 서버 시작. 포트 {PORT}에서 대기 중...")

conn, addr = server.accept()
print(f"클라이언트 연결됨: {addr}")

try:
    while True:
        data = conn.recv(1024)
        if not data:
            break
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
    pass
finally:
    conn.close()
    server.close()
    with open("tcp_recv_log.csv", "w") as f:
        for log in RECEIVED_LOG:
            f.write(','.join(map(str, log)) + '\n')
    print("수신 종료. tcp_recv_log.csv 저장 완료.")