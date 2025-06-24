import array
import socket
import rtmidi

# UDP 소켓 서버
UDP_IP = "0.0.0.0"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
print(f"Running Server..")

# MIDI 출력 포트
midi_out = rtmidi.MidiOut()
port_count = midi_out.get_port_count()

if port_count > 0:
    midi_out.open_port(0)
    print("MIDI Port Opened")
else:
    midi_out.open_visual_port("UDP MIDI Receiver")
    print("Opened virtual MIDI port (no hardware port found)")

# 수신 루프
try:
    while True:
        data, addr = sock.recvfrom(1024)  # 최대 1024바이트
        midi_msg = array.array('B', data[:3])
        print(f"Received from {addr}: {list(midi_msg)}")
        
        # MIDI 형식 검증
        if len(midi_msg) == 3 and midi_msg[0] & 0xF0 == 0x90:
            midi_out.send_message(midi_msg)
            print("✅ MIDI Note sent:", list(midi_msg))
        else:
            print("Invalid MIDI message format")

except KeyboardInterrupt:
    print("Stopping Server..")

finally:
    midi_out.closePort()