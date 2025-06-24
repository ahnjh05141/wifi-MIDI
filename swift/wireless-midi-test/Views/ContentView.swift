//
//  ContentView.swift
//  wireless-midi-test
//
//  Created by Anthony on 6/22/25.
//

import SwiftUI

struct ContentView: View {
    @State private var selectedInstrument: String = "Test"
    
    let midiManager = MIDIManager()
    
    private let intruments = ["Test", "Piano", "Drums"]
    
    var body: some View {
        VStack {
            Picker("Choose a color", selection: $selectedInstrument) {
                ForEach(intruments, id: \.self) {
                    Text($0)
                }
            }
            .pickerStyle(.segmented)
            .padding()
            .cornerRadius(15)
            .padding(10)
            
            switch selectedInstrument {
            case "Test":
                TestView()
            case "Piano":
                PianoView(midiManager: midiManager)
            case "Drums":
                DrumView(midiManager: midiManager)
            default:
                Text("No instrument selected")
            }
            
            Spacer()
        }
    }
}
