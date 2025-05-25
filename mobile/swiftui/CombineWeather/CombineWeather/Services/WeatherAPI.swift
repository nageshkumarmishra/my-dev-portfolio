//
//  WeatherAPI.swift
//  CombineWeather
//
//  Created by Nagesh Kumar Mishra on 16/05/25.
//

import Foundation
import Combine

class WeatherAPI {
    static func fetchCoordinates(for city: String) -> AnyPublisher<GeoLocation, Error> {
        let query = city.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed) ?? city
        let url = URL(string: "https://geocoding-api.open-meteo.com/v1/search?name=\(query)&count=1")!

        return URLSession.shared.dataTaskPublisher(for: url)
            .map(\.data)
            .decode(type: GeoResponse.self, decoder: JSONDecoder())
            .tryMap { response in
                guard let location = response.results.first else {
                    throw URLError(.badServerResponse)
                }
                return location
            }
            .eraseToAnyPublisher()
    }

    static func fetchWeather(for city: String) -> AnyPublisher<Weather, Error> {
        return fetchCoordinates(for: city)
            .flatMap { location in
                let url = URL(string: "https://api.open-meteo.com/v1/forecast?latitude=\(location.latitude)&longitude=\(location.longitude)&current_weather=true")!
                return URLSession.shared.dataTaskPublisher(for: url)
                    .map(\.data)
                    .decode(type: WeatherResponse.self, decoder: JSONDecoder())
                    .map(\.current_weather)
            }
            .receive(on: DispatchQueue.main)
            .eraseToAnyPublisher()
    }
}
