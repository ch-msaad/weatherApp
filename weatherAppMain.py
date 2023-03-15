import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        city_label = QLabel('City')
        self.city_entry = QLineEdit()
        country_label = QLabel('Country')
        self.country_entry = QLineEdit()
        self.button = QPushButton('Get Weather')
        self.result_label = QLabel()
        self.result_label.setAlignment(Qt.AlignCenter)  # fix here

        vbox = QVBoxLayout()
        vbox.addWidget(city_label)
        vbox.addWidget(self.city_entry)
        vbox.addWidget(country_label)
        vbox.addWidget(self.country_entry)
        vbox.addWidget(self.button)
        vbox.addWidget(self.result_label)

        self.setLayout(vbox)

        self.button.clicked.connect(self.show_weather)

        self.setWindowTitle('Weather App')
        self.show()

    def show_weather(self):
        city = self.city_entry.text()
        country = self.country_entry.text()
        weather_data = get_weather(city, country)

        if weather_data is None:
            self.result_label.setText('Error retrieving weather data')
        else:
            self.result_label.setText(f'Temperature: {weather_data["temperature"]} K\nHumidity: {weather_data["humidity"]}%\nDescription: {weather_data["description"]}')


def get_weather(city, country):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid=33d2ce0e0a01361aea11fafc3cc630a4'

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return None

    data = response.json()

    if data['cod'] != 200:
        return None

    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']

    return {'temperature': temperature, 'humidity': humidity, 'description': description}


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WeatherApp()
    sys.exit(app.exec_())
