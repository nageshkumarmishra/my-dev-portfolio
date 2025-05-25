//
//  WeatherViewModel.swift
//  CombineWeather
//
//  Created by Nagesh Kumar Mishra on 16/05/25.
//

import Foundation
import Combine

class WeatherViewModel: ObservableObject {
    @Published var city: String = ""
    @Published var matchedCity: String? = nil
    @Published var weather: Weather?
    @Published var errorMessage: String?
    @Published var isLoading = false

    private var cancellables = Set<AnyCancellable>()

    init() {
        $city
            .debounce(for: .milliseconds(500), scheduler: DispatchQueue.main)
            .removeDuplicates()
            .sink { [weak self] city in
                self?.getWeather(for: city)
            }
            .store(in: &cancellables)
    }

    func getWeather(for city: String) {
        guard !city.isEmpty else { return }

        isLoading = true
        errorMessage = nil
        weather = nil

        WeatherAPI.fetchWeather(for: city)
            .sink { [weak self] completion in
                self?.isLoading = false
                if case .failure(let error) = completion {
                    self?.errorMessage = error.localizedDescription
                }
            } receiveValue: { [weak self] weather in
                self?.weather = weather
                self?.matchedCity = city.capitalized
            }
            .store(in: &cancellables)
    }
}
