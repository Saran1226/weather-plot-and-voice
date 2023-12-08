# Хүсэлт илгээх учраас доорх санг дуудаж байна.
import requests 

# Класс зарлаж байна.
class Weather: 
    # Байгуулагч функц дуудаж байна.
    def __init__(self, city):
        # Одоогийн цаг агаар авах холбоос
        CURRENT_BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
        # Дараачийн 5 өдрийн цаг агаар авах холбоос
        FORECAST_BASE_URL = "http://api.openweathermap.org/data/2.5/forecast?"
        # Хүсэлт илгээхдээ ашиглах нууц түлхүүрээ бичиж байна
        API_KEY = "ac24d3fd435ae9a931e268819ad98cb0"

        # Цаг агаар авах холбоосдоо өөрсдийн параметрүүдээ нэмж байна
        self.current_url = CURRENT_BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=metric"
        self.forecast_url = FORECAST_BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=metric"

    def getCurrentWeather(self):
        # Энэ функц бол одоогийн цаг агаар авах функц
        # Ингэхдээ одоогийн цаг агаар авах холбоосруу 
        # хүсэлт илгээж хариуг буцаана
        response = requests.get(self.current_url).json()
        
        return response
    
    def getForecastWeather(self):
        # Энэ функц бол дараачийн 5 өдрийн цаг агаар авах функц
        # Ингэхдээ дараачийн 5 өдрийн цаг агаар авах холбоосруу 
        # хүсэлт илгээж хариуг буцаана
        response = requests.get(self.forecast_url).json()
        
        return response