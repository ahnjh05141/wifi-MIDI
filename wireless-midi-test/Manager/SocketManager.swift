//
//  SocketManager.swift
//  wireless-midi-test
//
//  Created by Anthony on 6/22/25.
//

import Foundation
import Network

class SocketManager {
    private var counter = 0

    func sendUDPMessages(interval: TimeInterval = 0.01, count: Int = 10000) {
        counter = 0
        let endpoint = NWEndpoint.Host("192.168.0.51")
        let nwPort = NWEndpoint.Port(rawValue: 5005)!
        let connection = NWConnection(host: endpoint, port: nwPort, using: .udp)
        connection.start(queue: .main)

        Timer.scheduledTimer(withTimeInterval: interval, repeats: true) { [weak self] t in
            guard let self = self else { return }
            let timestamp = Date().timeIntervalSince1970
            let message = String(format: "%d,%.6f", self.counter, timestamp)
            connection.send(content: message.data(using: .utf8), completion: .contentProcessed({ _ in }))
            self.counter += 1
            if self.counter > count {
                t.invalidate()
                connection.cancel()
                print("UDP sending completed.")
            }
        }
    }

    func sendTCPMessages(interval: TimeInterval = 0.01, count: Int = 10000) {
        counter = 0
        let endpoint = NWEndpoint.Host("192.168.0.51")
        let nwPort = NWEndpoint.Port(rawValue: 5005)!
        let connection = NWConnection(host: endpoint, port: nwPort, using: .tcp)
        connection.start(queue: .main)

        Timer.scheduledTimer(withTimeInterval: interval, repeats: true) { [weak self] t in
            guard let self = self else { return }
            let timestamp = Date().timeIntervalSince1970
            let message = String(format: "%d,%.6f", self.counter, timestamp)
            connection.send(content: message.data(using: .utf8), completion: .contentProcessed({ _ in }))
            self.counter += 1
            if self.counter > count {
                t.invalidate()
                connection.cancel()
                print("TCP sending completed.")
            }
        }
    }
}
