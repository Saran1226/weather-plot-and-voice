from weather import Weather
from data_processor import DataProcessor
from text_to_speech import TextToSpeech
from dashboard import Dashboard

# Энэ файл бол үндсэн файл ба 
# эндээс бусад классуудыг дуудаж ажиллуулж байна.


CITY = "Budapest"

# Weather класс үүсгэж байна
weather = Weather(CITY)
# Классын getCurrentWeather функцийг дуудаж одоогийн 
# цаг агаарыг авч байна.
current_response = weather.getCurrentWeather()
# Классын getCurrentWeather функцийг дуудаж дараачийн 
# 5 өдрийн цаг агаарыг авч байна.
forecast_response = weather.getForecastWeather()


# print(current_response)

# DataProcessor класс үүсгэж байна
dataProcessor = DataProcessor()

# Классын process_data функцийг дуудаж цаг агаарын 
# өгөгдлийг боловсруулж байна.
# Ингэхдээ одоогийн цаг агаар, дараачийн 5 өдрийн 
# цаг агаарыг дамжуулж байна.
data = dataProcessor.process_data(current_response, forecast_response)

# Боловсруулсан хариуг хэвлэж үзэж байна.
print(data)


# Текст унших класс үүсгэж байна.
tts = TextToSpeech()
# Унших текстийг дамжуулж өгч байна
text_to_read = data['now_text'] + data['forecast_text']
tts.generate_audio(text_to_read)

# хянах самбар класс үүсгэж байна
dashboard = Dashboard()
# Хянах самбар үзүүлэх функцийг дуудаж байна. 
# Ингэхдээ, аль хэдийн боловсруулсан дараачийн 
# 5 өдрийн цаг агаарын өгөгдөл дамжуулж байна.
dashboard.display_dashboard(data['temperatures_in_5days'])