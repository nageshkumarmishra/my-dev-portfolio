//
//  LottieView.swift
//  CombineWeather
//
//  Created by Nagesh Kumar Mishra on 16/05/25.
//

import Foundation
import SwiftUI
import Lottie

struct LottieView: UIViewRepresentable {
    var filename: String

    func makeUIView(context: Context) -> LottieAnimationView {
        let view = LottieAnimationView(name: filename)
        view.loopMode = .loop
        view.play()
        return view
    }

    func updateUIView(_ uiView: LottieAnimationView, context: Context) {}
}

