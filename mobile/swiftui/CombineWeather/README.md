
# 🌦️ CombineWeather — SwiftUI iOS Weather App

**CombineWeather** is a lightweight, elegant iOS weather application built using **SwiftUI**, **Combine**, and the **MVVM** architecture pattern. It showcases best practices in modular iOS development and reactive UI design using modern Swift features.

---

## 📱 Features

- 🔍 Fetches current weather based on user’s location
- 🌤️ Displays animated weather conditions using **Lottie**
- 🧩 Clean architecture using **Model-View-ViewModel (MVVM)**
- 🚀 Fully SwiftUI-native and Combine-enabled
- 🧪 Includes both Unit and UI tests

---

## 🧱 Tech Stack

| Layer        | Technology |
|--------------|------------|
| UI           | SwiftUI    |
| State Mgmt   | Combine    |
| Architecture | MVVM       |
| Animation    | Lottie     |
| Location     | CoreLocation |
| Networking   | URLSession |

---

## 📂 Project Structure

```
CombineWeather/
├── CombineWeatherApp.swift       # App entry point
├── ContentView.swift             # Base container
├── Views/
│   ├── WeatherView.swift         # Weather UI components
│   ├── LottieView.swift          # Lottie animation wrapper
├── ViewModels/
│   ├── WeatherViewModel.swift    # Observable view model
├── Models/
│   ├── GeoLocation.swift         # User location model
│   ├── Weather.swift             # Weather response model
├── Services/
│   ├── WeatherAPI.swift          # API handler using Combine
├── Resources/
│   ├── rain.json, thunderstorm.json, cloud.json  # Lottie assets
│   ├── Assets.xcassets/
├── CombineWeatherTests/         # Unit tests
├── CombineWeatherUITests/       # UI tests
```

---

## 🚀 Getting Started

### 🧰 Requirements

- Xcode 14+
- iOS 15+
- Swift 5.7+

### 🛠 Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/my-dev-portfolio.git
   cd my-dev-portfolio/mobile/combine-weather
   ```

2. Open the `.xcodeproj` or `.xcworkspace` in Xcode.

3. Run the app in a simulator or real device.

---

## 🧪 Testing

You’ll find both unit and UI tests under:

- `CombineWeatherTests/`
- `CombineWeatherUITests/`

Run via `CMD + U` in Xcode.

---

## 🖼️ Screenshots

> _You can include screenshots here in future: `/screenshots/` folder and embed with Markdown._

---

## 🙋‍♂️ Author

**Nagesh Kumar Mishra**  
🔗 [LinkedIn](https://linkedin.com/in/nageshkumarmishra) | 🐙 [GitHub](https://github.com/nageshkumarmishra)

---

> This project is part of [My Dev Portfolio](https://github.com/nageshkumarmishra/my-dev-portfolio)
