import unittest

from weather import Weather
from data_processor import DataProcessor
from text_to_speech import TextToSpeech
from dashboard import Dashboard

import numpy as np
import matplotlib.pyplot as plt


class Tests(unittest.TestCase):
    def test_weather(self):
        weather= Weather("Budapest")

        current = weather.getCurrentWeather()
        forecast = weather.getForecastWeather()
        
        self.assertTrue(isinstance(current, dict))
        self.assertTrue(isinstance(forecast, dict))
        
        self.assertTrue(current['main'] is not None)
        self.assertTrue(len(forecast['list']) > 0)

        # dataProcess 
        dataProcessor = DataProcessor()

        data = dataProcessor.process_data(current, forecast)
        
        self.assertTrue(isinstance(data, dict))
        
        
        self.assertTrue('now' in data)
        self.assertTrue('now', int in data)
        self.assertTrue('average_in_5days' in data)
        self.assertTrue('average_in_5days', int in data)
        self.assertTrue('highest_in_5days' in data)
        self.assertTrue('highest_in_5days', int in data)
        self.assertTrue('lowest_in_5days' in data)
        self.assertTrue('lowest_in_5days', int in data)
        self.assertTrue('now_text' in data)
        self.assertTrue('now_text', str in data)
        self.assertTrue('forecast_text' in data)
        self.assertTrue('forecast_text', str in data)
        self.assertTrue('temperatures_in_5days' in data)
        self.assertTrue('temperatures_in_5days', list in data)

if __name__ == '__main__':
    unittest.main()


