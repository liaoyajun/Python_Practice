import requests
import threading

def get_weather(city):
    req = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s' % city)
    dic_city = req.json()

    city_data = dic_city.get('data')
    print(city_data.get('city'))

    if city_data:
        city_forecast = city_data['forecast'][0]
        print(city_forecast.get('date'))
        print(city_forecast.get('high'))
        print(city_forecast.get('low'))
        print(city_forecast.get('type'))
    else:
        print('未获得')
    print()


threads = []
cities = ['北京', '南京', '上海', '深圳', '广州', '杭州', '苏州', '天津', '西安', '成都']
files = range(len(cities))
for i in files:
    t = threading.Thread(target=get_weather, args=(cities[i],))
    threads.append(t)
for i in files:
    threads[i].start()
for i in files:
    threads[i].join()
print('结束获取')