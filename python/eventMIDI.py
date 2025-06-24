import socket
import rtmidi

# MIDI 출력 설정
midi_out = rtmidi.MidiOut()
if midi_out.get_port_count() > 0:
    midi_out.open_port(0)
    print("✅ Opened MIDI Output Port")
else:
    midi_out.openVirtualPort("Virtual MIDI Sender")
    print("🎹 Opened Virtual MIDI Port")

# 전송할 MIDI (C4 note on)
note_on = [0x90, 60, 100]

# 송신 대상
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 메시지 전송
sock.sendto(bytes(note_on), (UDP_IP, UDP_PORT))
print(f"📤 Sent MIDI message {note_on} to {UDP_IP}:{UDP_PORT}")

sock.close()