//
//  InstrumentView.swift
//  wireless-midi-test
//
//  Created by Anthony on 6/22/25.
//

import SwiftUI

struct DrumView: View {
    
    let midiManager: MIDIManager
    
    var body: some View {
        GeometryReader { geometry in
            let columns = 2
            let rows = 3
            let spacing: CGFloat = 2
            let buttonWidth = (geometry.size.width - spacing * CGFloat(columns - 1)) / CGFloat(columns)
            let buttonHeight = (geometry.size.height - spacing * CGFloat(rows - 1)) / CGFloat(rows)

            VStack(spacing: spacing) {
                ForEach(0..<rows, id: \.self) { row in
                    HStack(spacing: spacing) {
                        ForEach(0..<columns, id: \.self) { col in
                            Button(action: {
                                let note = UInt8(36 + row * columns + col)
                                midiManager.sendNoteOn(note: note, velocity: 100)
                            }) {
                                Text("Pad \(row * columns + col + 1)")
                                    .frame(width: buttonWidth, height: buttonHeight)
                                    .background(Color.blue)
                                    .foregroundColor(.white)
                                    .cornerRadius(10)
                            }
                        }
                    }
                }
            }
        }
    }
}
