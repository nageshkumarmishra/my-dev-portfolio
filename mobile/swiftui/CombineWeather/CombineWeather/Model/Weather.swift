//
//  Weather.swift
//  CombineWeather
//
//  Created by Nagesh Kumar Mishra on 16/05/25.
//

import Foundation

struct Weather: Decodable {
    let temperature: Double
    let windspeed: Double
    let weathercode: Int
}

struct WeatherResponse: Decodable {
    let current_weather: Weather
}

