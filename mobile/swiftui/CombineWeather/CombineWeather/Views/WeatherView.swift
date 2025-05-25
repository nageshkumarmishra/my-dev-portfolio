//
//  WeatherView.swift
//  CombineWeather
//
//  Created by Nagesh Kumar Mishra on 16/05/25.
//

import Foundation
import SwiftUI

struct WeatherView: View {
    @StateObject private var viewModel = WeatherViewModel()
    @State private var showLightning = false
    @State private var rainDropOffset: CGFloat = -100
    @State private var cloudOffset: CGFloat = -150
    
    var body: some View {
        NavigationView {
            ZStack {
                LinearGradient(
                    gradient: Gradient(colors: [Color.blue.opacity(0.2), Color.white]),
                    startPoint: .top,
                    endPoint: .bottom
                )
                .ignoresSafeArea()
                
                VStack(spacing: 20) {
                    VStack(alignment: .leading, spacing: 8) {
                        Text("🌍 Enter City")
                            .font(.headline)
                            .accessibilityLabel("Enter city label")
                        TextField("e.g. London", text: $viewModel.city)
                            .padding()
                            .background(RoundedRectangle(cornerRadius: 8).fill(Color.white))
                            .shadow(radius: 1)
                            .accessibilityIdentifier("cityTextField")
                    }
                    .padding()
                    
                    if viewModel.isLoading {
                        ProgressView("Fetching weather...")
                            .progressViewStyle(CircularProgressViewStyle())
                            .padding()
                            .accessibilityIdentifier("loadingIndicator")
                    }
                    
                    if let weather = viewModel.weather {
                        if let city = viewModel.matchedCity {
                            Text("📍 Weather in \(city)")
                                .font(.title2)
                                .bold()
                                .padding()
                                .frame(maxWidth: .infinity)
                                .background(RoundedRectangle(cornerRadius: 10).fill(Color.white.opacity(0.6)))
                                .padding(.horizontal)
                                .accessibilityIdentifier("matchedCityLabel")
                        }
                        
                        ZStack {
                            if (weather.weathercode == 95 || weather.weathercode == 96) {
                                LottieView(filename: "thunderstorm")
                                    .frame(width: 150, height: 150)
                            }
                            
                            if (weather.weathercode == 61 || weather.weathercode == 63 || weather.weathercode == 65) {
                                LottieView(filename: "rain")
                                    .frame(width: 150, height: 150)
                            }
                            
                            if weather.weathercode == 2 {
                                LottieView(filename: "cloud")
                                    .frame(width: 150, height: 150)
                            }
                        }
                        
                        VStack(spacing: 16) {
                            HStack {
                                Image(systemName: "thermometer.sun.fill")
                                    .foregroundColor(.orange)
                                Text("Temperature:")
                                Spacer()
                                Text("\(weather.temperature, specifier: "%.1f") °C")
                                    .bold()
                            }
                            
                            HStack {
                                Image(systemName: "wind")
                                    .foregroundColor(.blue)
                                Text("Wind Speed:")
                                Spacer()
                                Text("\(weather.windspeed, specifier: "%.1f") km/h")
                                    .bold()
                            }
                            
                            HStack {
                                Image(systemName: "cloud.sun.fill")
                                    .foregroundColor(.gray)
                                Text("Weather Code:")
                                Spacer()
                                Text("\(weather.weathercode)")
                                    .bold()
                            }
                        }
                        .padding()
                        .background(RoundedRectangle(cornerRadius: 12).fill(Color.white))
                        .shadow(radius: 2)
                        .padding(.horizontal)
                        .accessibilityElement(children: .combine)
                        .accessibilityIdentifier("weatherDetails")
                    }
                    
                    if let error = viewModel.errorMessage {
                        Text("❌ \(error)")
                            .foregroundColor(.white)
                            .padding()
                            .frame(maxWidth: .infinity)
                            .background(Color.red)
                            .cornerRadius(10)
                            .padding(.horizontal)
                            .accessibilityIdentifier("errorMessage")
                    }
                    
                    Spacer()
                }
                .navigationTitle("🌦 Weather Checker")
            }
        }
    }
}
struct LightningView: View {
    @Binding var isFlashing: Bool

    var body: some View {
        Image(systemName: "cloud.bolt.rain.fill")
            .resizable()
            .scaledToFit()
            .frame(width: 80, height: 80)
            .foregroundColor(.yellow)
            .opacity(isFlashing ? 1 : 0)
            .animation(Animation.easeInOut(duration: 0.3).repeatForever(autoreverses: true), value: isFlashing)
            .onAppear { isFlashing = true }
    }
}

struct RainView: View {
    @Binding var dropOffset: CGFloat

    var body: some View {
        ZStack {
            ForEach(0..<6, id: \.self) { i in
                Image(systemName: "drop.fill")
                    .foregroundColor(.blue)
                    .opacity(0.5)
                    .offset(y: dropOffset)
                    .animation(Animation.linear(duration: 1.5).repeatForever().delay(Double(i) * 0.2), value: dropOffset)
            }
        }
        .onAppear {
            dropOffset = 200
        }
    }
}

struct CloudView: View {
    @Binding var cloudOffset: CGFloat

    var body: some View {
        Image(systemName: "cloud.fill")
            .resizable()
            .frame(width: 100, height: 60)
            .foregroundColor(.gray)
            .offset(x: cloudOffset)
            .animation(Animation.linear(duration: 10).repeatForever(autoreverses: false), value: cloudOffset)
            .onAppear {
                cloudOffset = 150
            }
    }
}
