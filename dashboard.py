#main-ees haruulah functioniig duudaj baigaa
#grapic haruulah heseg.
# График үзүүлэхийн тулд matplotlib санг дуудж байна
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Класс үүсгэж байна
class Dashboard:
    # Өөрт өгөгдөл хадгалах, тохиргоо хийх хэрэггүй болохоор байгуулагч функц хэрэггүй

    # График үзүүлэх функц
    def display_dashboard(self, data_points):
        # дамжуулсан өгөгдлөөс огноо, темпаратурийг салгаж авч байна.
        # Учир нь data_points [("Sunday 17", 10), ("Sunday 20", 8), ...] ийм форматтай 
        # Үүнийг timestamps ['Sunday 17', 'Sunday 20', ...]
        # temperatures [10, 8, ...] гэсэн хоёр хүснэгт болгож байна.
        timestamps = [date for date, _ in data_points]
        temperatures = [temp for _, temp in data_points]

        # график үзүүлэхэд хэрэгтэй баахан функцууд
        plt.figure(figsize=(15, 15))
        plt.plot(timestamps, temperatures, marker='o')
        plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)
        plt.xlabel("Date time")
        plt.ylabel("Temperature")
        plt.title("Forecast Data")
        plt.xticks(rotation=45)
        plt.grid()
        plt.show()

