# City Statistics (Live Weather & Location)

A lightweight Python desktop application built with Tkinter that fetches real-time geographical coordinates and live weather statistics for any city in the world using the Open-Meteo API.

## 🌍 Features
* **Clean Desktop GUI:** Built with Tkinter for a simple, intuitive window interface with instant status and error feedback.
* **Global City Search:** Uses Open-Meteo's Geocoding API to look up any city worldwide and retrieve its country, latitude, and longitude.
* **Live Weather Data:** Connects to Open-Meteo's Forecast API to fetch real-time temperature data with automatic unit formatting.
* **Input Validation:** Automatically checks for valid alphabetical city names and handles missing database entries gracefully without crashing.
* **No API Key Required:** Uses Open-Meteo's free, open-source REST APIs with zero sign-up or authentication needed.

## 🚀 How to Use

### Option 1: Windows Executable (No Python Required)
1. Go to the **Releases** section on the right side of this page.
2. Download the **`.zip`** file under **Assets** and extract it.
3. Double-click **`city_statistics.exe`**, enter any city name, and click **Get Statistics of City** to view live coordinates and temperature.

### Option 2: Run via Python
1. Clone or download this repository (`city_statistics.py`).
2. Install the required `requests` library:
   ```bash
   pip install requests
   ```
3. Run the script in your terminal or IDE:
   ```bash
   python city_statistics.py
   ```
