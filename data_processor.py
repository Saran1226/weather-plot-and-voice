# Grapic bolon audio filuudad ashiglah ugugdiig beldej ugnu
# Энд өгөгдөл боловсруулах statistics сан болон 
# огноо боловсруулах datetime санг дуудаж байна
import statistics
from datetime import datetime

# Класс зарлаж байна
class DataProcessor:
    # Дамжуулсан өгөгдлийг боловсруулаад шууд буцаах тул
    # өөртөө өгөгдөл хадгалах шаардлагагүй.
    # Тийм учраас байгуулагч функц __init__ зарлахгүй.  
    

    # Энэ бол өгөгдөл боловсруулах функц
    # Энэ функцруу одоогийн болон дараачийн 5 өдрийн цаг агаарыг
    # тус тусд нь дамжуулах ёстой. 
    def process_data(self, current, forecast):
        # Хэрэв одоогийн цаг агаар байхгүй бол алдаа заана
        if not current:
            print("No current data available for processing.")
            return

        # Цаг агаарын өгөгдөл хадгалах хоосон list зарлаж байна.
        temperatures = []
        temperatures_in_5days = []
        
        # Энэ коммандаар ямар өгөгдөл боловсруулах гэж буйг харж болно.
        # print(forecast['list'])

        # Дараачийн 5 өдрийн өгөгдөл list дотор байгаа 
        # учраас давталт ашиглах гэж байна
        for item in forecast['list']:
            # dt элементээс огнооны цагийг авна
            timestamp = item['dt']
            # Цагийн зөрүүг нэмж байна
            date_obj = datetime.fromtimestamp(timestamp + forecast['city']['timezone'])
            # Огноог Долоо хоногийн өдөр болон цагийн форматтай стринг болгож байна
            date = date_obj.strftime('%A %H')
            # өгөгдлөөс темпаратурыг салгаж авч байна
            temperature = item['main']['temp']
            # Бүхэл тоо руу хөрвүүлж байна
            temperature_int = int(temperature)
            
            # Өмнө зарласан list-үүдрүү нэмж байна
            temperatures.append(temperature_int)
            temperatures_in_5days.append((date, temperature_int)) 

        # print(temperatures, temperatures_in_5days)
        
        # одоогийн темпаратурыг бүхэл тооруу шилжүүлж байна.
        now = int(current['main']['temp'])
        # statistics санг ашиглаж дундаж утга олж байна
        average_in_5days = round(statistics.mean(temperatures), 2)
        # дараачийн 5 өдрийн хамгийн их утга
        highest_in_5days = max(temperatures)
        # дараачийн 5 өдрийн хамгийн бага утга
        lowest_in_5days = min(temperatures)
        

        # Боловсруулсан өгөгдлүүдээ нийлүүлээд нэг объект болгож байна
        # энд now_text, forecast_text элементүүд нь унших текстүүд байх юм.
        data = {
            "now": now,
            "average_in_5days": average_in_5days,
            "highest_in_5days": highest_in_5days,
            "lowest_in_5days": lowest_in_5days,
            "now_text": "It's currently " + str(now) + " degrees in Budapest.",
            "forecast_text": "In the next 5 days, the highest is " + str(highest_in_5days) + " and lowest is " + str(lowest_in_5days) + " degrees.",            
            "temperatures_in_5days": temperatures_in_5days,
        }

        return data
    



# Цаг агаарын өгөгдлийн бүтэц ингэж харагдаж байгаа
# {
#   "list": [
#     {
#       "dt": 1661871600,
#       "main": {
#         "temp": 296.76,
#       },
#     },