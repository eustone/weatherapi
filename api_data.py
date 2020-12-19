{'coord': {'lon': 28.29, 'lat': -15.41}, 
'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}],
'base': 'stations', 
'main': {'temp': 296.15, 'feels_like': 298.31, 'temp_min': 296.15, 'temp_max': 296.15, 'pressure': 1015, 'humidity': 78},
'visibility': 10000, 'wind': {'speed': 1.5, 'deg': 50}, 
'rain': {'1h': 0.17}, 'clouds': {'all': 75}, 'dt': 1607961802, 
'sys': {'type': 1, 'id': 2113, 'country': 'ZM', 'sunrise': 1607916645, 'sunset': 1607963560},
'timezone': 7200, 'id': 909137, 'name': 'Lusaka', 'cod': 200}


dt = {'main': {'temp': 296.15, 'feels_like': 298.31,
              'temp_min': 296.15, 'temp_max': 296.15, 'pressure': 1015, 'humidity': 78}}

print(dt['main']['temp_max'])
