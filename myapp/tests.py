import json

array = [{"model": "myapp.weather", "pk": 533,
      "fields": {"city": 2, "time": 1480410000, "temperature_max": -9.42, "temperature_min": -9.42,
                 "temperature_day": -9.42, "temperature_night": -9.42, "wind": 6.22, "cloudiness": 64,
                 "pressure": 1019.79, "description": "clear sky"}}, {"model": "myapp.weather", "pk": 534,
                                                                     "fields": {"city": 2, "time": 1480496400,
                                                                                "temperature_max": -2.52,
                                                                                "temperature_min": -8.23,
                                                                                "temperature_day": -6.39,
                                                                                "temperature_night": -2.52,
                                                                                "wind": 3.32, "cloudiness": 0,
                                                                                "pressure": 1022,
                                                                                "description": "light snow"}},
     {"model": "myapp.weather", "pk": 535,
      "fields": {"city": 2, "time": 1480582800, "temperature_max": 1.13, "temperature_min": -1.4,
                 "temperature_day": 0.67, "temperature_night": -1.4, "wind": 4.71, "cloudiness": 80,
                 "pressure": 1007.22, "description": "light snow"}}, {"model": "myapp.weather", "pk": 536,
                                                                      "fields": {"city": 2, "time": 1480669200,
                                                                                 "temperature_max": 2.52,
                                                                                 "temperature_min": -3.92,
                                                                                 "temperature_day": 0.78,
                                                                                 "temperature_night": -3.92,
                                                                                 "wind": 7.97, "cloudiness": 92,
                                                                                 "pressure": 986.6,
                                                                                 "description": "snow"}},
     {"model": "myapp.weather", "pk": 537,
      "fields": {"city": 2, "time": 1480755600, "temperature_max": -2.46, "temperature_min": -3.48,
                 "temperature_day": -2.55, "temperature_night": -3.48, "wind": 10.23, "cloudiness": 89,
                 "pressure": 1003.75, "description": "snow"}}, {"model": "myapp.weather", "pk": 538,
                                                                "fields": {"city": 2, "time": 1480842000,
                                                                           "temperature_max": -3.7,
                                                                           "temperature_min": -9.92,
                                                                           "temperature_day": -3.7,
                                                                           "temperature_night": -9.92, "wind": 4.04,
                                                                           "cloudiness": 48, "pressure": 1023.2,
                                                                           "description": "light snow"}},
     {"model": "myapp.weather", "pk": 539,
      "fields": {"city": 2, "time": 1480928400, "temperature_max": -2.89, "temperature_min": -11.8,
                 "temperature_day": -5.7, "temperature_night": -2.89, "wind": 4.52, "cloudiness": 30,
                 "pressure": 1031.48, "description": "light snow"}}, {"model": "myapp.weather", "pk": 540,
                                                                      "fields": {"city": 2, "time": 1481014800,
                                                                                 "temperature_max": 3.41,
                                                                                 "temperature_min": -1.12,
                                                                                 "temperature_day": 2.3,
                                                                                 "temperature_night": 3.41,
                                                                                 "wind": 8.52, "cloudiness": 100,
                                                                                 "pressure": 1010.05,
                                                                                 "description": "snow"}},
     {"model": "myapp.weather", "pk": 541,
      "fields": {"city": 2, "time": 1481101200, "temperature_max": 1.14, "temperature_min": -4.89,
                 "temperature_day": 1.14, "temperature_night": -4.89, "wind": 6.89, "cloudiness": 50,
                 "pressure": 1004.75, "description": "snow"}}, {"model": "myapp.weather", "pk": 542,
                                                                "fields": {"city": 2, "time": 1481187600,
                                                                           "temperature_max": -1.42,
                                                                           "temperature_min": -6.45,
                                                                           "temperature_day": -4.5,
                                                                           "temperature_night": -1.42, "wind": 4.84,
                                                                           "cloudiness": 65, "pressure": 1022.41,
                                                                           "description": "light snow"}},
     {"model": "myapp.weather", "pk": 543,
      "fields": {"city": 2, "time": 1481274000, "temperature_max": 3.97, "temperature_min": 1.21,
                 "temperature_day": 3.97, "temperature_night": 1.21, "wind": 6.08, "cloudiness": 85, "pressure": 1010.5,
                 "description": "light snow"}}, {"model": "myapp.weather", "pk": 544,
                                                 "fields": {"city": 2, "time": 1481360400, "temperature_max": 5.18,
                                                            "temperature_min": 1.56, "temperature_day": 4.41,
                                                            "temperature_night": 5.18, "wind": 7, "cloudiness": 98,
                                                            "pressure": 1009.23, "description": "light rain"}},
     {"model": "myapp.weather", "pk": 545,
      "fields": {"city": 2, "time": 1481446800, "temperature_max": 7.04, "temperature_min": 3.7,
                 "temperature_day": 7.04, "temperature_night": 3.7, "wind": 7.92, "cloudiness": 100, "pressure": 1004.4,
                 "description": "light rain"}}, {"model": "myapp.weather", "pk": 546,
                                                 "fields": {"city": 2, "time": 1481533200, "temperature_max": 3.42,
                                                            "temperature_min": -1.64, "temperature_day": 3.42,
                                                            "temperature_night": -1.64, "wind": 14.55, "cloudiness": 90,
                                                            "pressure": 993.57, "description": "light snow"}}]

data  = json.loads(str(array))
fruits_list = data['fruits']
print(fruits_list)