from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPixmap
from weatherAppMain import get_weather

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # Set the title and window size
        self.setWindowTitle('Weather App')
        self.setGeometry(200, 200, 500, 400)
        
        # Create the UI components
        self.city_label = QLabel('City:', self)
        self.city_entry = QLineEdit(self)
        self.country_label = QLabel('Country:', self)
        self.country_entry = QLineEdit(self)
        self.get_weather_button = QPushButton('Get Weather', self)
        self.result_label = QLabel(self)
        self.result_label.setWordWrap(True)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setFixedHeight(150)
        self.icon_label = QLabel(self)
        
        # Create a vertical layout for the UI components
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_entry)
        vbox.addWidget(self.country_label)
        vbox.addWidget(self.country_entry)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.result_label)
        vbox.addWidget(self.icon_label)
        
        # Set the layout of the main window
        self.setLayout(vbox)
        
        # Connect the button to the function that retrieves the weather data
        self.get_weather_button.clicked.connect(self.show_weather)
    
    def show_weather(self):
        city = self.city_entry.text()
        country = self.country_entry.text()
        weather_data = get_weather(city, country)

        if weather_data is None:
            self.result_label.setText('Error retrieving weather data')
            self.icon_label.clear()
        else:
            self.result_label.setText(f'Temperature: {weather_data["temperature"]} K\nHumidity: {weather_data["humidity"]}%\nDescription: {weather_data["description"]}')
            pixmap = QPixmap(f'icons/{weather_data["icon"]}.png')
            self.icon_label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication([])
    window = WeatherApp()
    window.show()
    app.exec_()
