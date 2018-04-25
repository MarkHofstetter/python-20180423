import requests
from pprint import pprint

def get_data_from_rest_api():
    url = 'http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22'
    response = requests.get(url)
    data = response.json()
    return data
    
def get_temperature_celsius_from_api_data(json_from_api):
    temp = json_from_api['main']['temp'] - 273.15
    return temp

def main():
    api_data = get_data_from_rest_api()
    temp = get_temperature_celsius_from_api_data(api_data)
    print("Temperatur: {:0.1f}".format(temp))
    
if __name__ == '__main__':
    main()

'''
{'base': 'stations',
 'clouds': {'all': 90},
 'cod': 200,
 'coord': {'lat': 51.51, 'lon': -0.13},
 'dt': 1485789600,
 'id': 2643743,
 'main': {'humidity': 81,
          'pressure': 1012,
          'temp': 280.32,
          'temp_max': 281.15,
          'temp_min': 279.15},
 'name': 'London',
 'sys': {'country': 'GB',
         'id': 5091,
         'message': 0.0103,
         'sunrise': 1485762037,
         'sunset': 1485794875,
         'type': 1},
 'visibility': 10000,
 'weather': [{'description': 'light intensity drizzle',
              'icon': '09d',
              'id': 300,
              'main': 'Drizzle'}],
 'wind': {'deg': 80, 'speed': 4.1}}
'''