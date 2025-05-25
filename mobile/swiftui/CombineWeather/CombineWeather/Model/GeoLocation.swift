//
//  GeoLocation.swift
//  CombineWeather
//
//  Created by Nagesh Kumar Mishra on 16/05/25.
//

import Foundation


struct GeoLocation: Decodable {
    let latitude: Double
    let longitude: Double
}

struct GeoResponse: Decodable {
    let results: [GeoLocation]
}
