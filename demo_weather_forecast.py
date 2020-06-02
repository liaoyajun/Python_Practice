# -*- coding: utf-8 -*-
# pycharm 命令行运行
# pip install requests
import requests

while True:
    city = input('请输入城市,回车退出:\n')
    if not city:
        break
    res = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s' % city)
    dic_city = res.json()
    city_data = dic_city.get('data')
    if city_data:
        city_forecast = city_data['forecast'][0]
        print(city_forecast.get('date'))
        print(city_forecast.get('high'))
        print(city_forecast.get('low'))
        print(city_forecast.get('type'))
    else:
        print('未获得')
