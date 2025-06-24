//
//  TestView.swift
//  wireless-midi-test
//
//  Created by Anthony on 6/24/25.
//

import SwiftUI

struct TestView: View {
    let socketManager = SocketManager()

    var body: some View {
        VStack(spacing: 20) {
            Button("Send UDP Messages") {
                socketManager.sendUDPMessages()
            }
            .padding()
            .background(Color.blue)
            .foregroundColor(.white)
            .cornerRadius(10)

            Button("Send TCP Messages") {
                socketManager.sendTCPMessages()
            }
            .padding()
            .background(Color.green)
            .foregroundColor(.white)
            .cornerRadius(10)
        }
        .padding()
    }
}
