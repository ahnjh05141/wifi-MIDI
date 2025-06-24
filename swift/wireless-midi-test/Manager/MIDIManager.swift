//
//  MIDIManager.swift
//  wireless-midi-test
//
//  Created by Anthony on 6/22/25.
//


import Foundation
import CoreMIDI

class MIDIManager {
    var client = MIDIClientRef()
    var outPort = MIDIPortRef()
    var destination: MIDIEndpointRef?

    init() {
        // 1. MIDI Client 생성
        MIDIClientCreate("MIDI Client" as CFString, nil, nil, &client)

        // 2. 출력 포트 생성
        MIDIOutputPortCreate(client, "Output Port" as CFString, &outPort)

        // 3. 네트워크 세션 활성화
        let session = MIDINetworkSession.default()
        session.isEnabled = true
        session.connectionPolicy = .anyone

        // 4. 첫 번째 네트워크 destination 가져오기
        destination = session.destinationEndpoint()
    }

    func sendNoteOn(note: UInt8 = 60, velocity: UInt8 = 100) {
        guard let destination = destination else {
            print("❌ No destination endpoint")
            return
        }

        // 5. MIDI 메시지 구성 (Note On)
        var packet = MIDIPacket()
        packet.timeStamp = 0
        packet.length = 3
        packet.data.0 = 0x90  // Note On
        packet.data.1 = note
        packet.data.2 = velocity

        var packetList = MIDIPacketList(numPackets: 1, packet: packet)

        // 6. 메시지 전송
        MIDISend(outPort, destination, &packetList)
        print("✅ Sent Note On: \(note)")
    }
}
