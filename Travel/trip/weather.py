#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/23 下午8:46
# @Author  : Kavin-lee
# @Email   : kavin_lee@yeah.net
# @File    : we.py
# @Software: PyCharm

# 爬取天气信息
import requests
from bs4 import BeautifulSoup


def KnowWeather(url):
    # url = 'http://www.weather.com.cn/weather/101110101.shtml'
    # url='http://www.weather.com.cn/weather/101110901.shtml'
    headers = {
        'Host': 'www.weather.com.cn',
        'User - Agent': 'Mozilla / 5.0(X11;Ubuntu;Linuxx86_64;rv: 67.0) Gecko / 20100101Firefox / 67.0',
        'Connection': 'keep - alive'
    }
    response = requests.get(url, headers=headers, verify=False)
    html = response.content.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser').body
    data = soup.find('div', {'id': '7d'})
    # print(data)
    ul = data.find('ul')
    # print(ul)
    li = ul.find_all('li')
    # print(li)

    findall_dict = {}
    for day in li:
        temp = []
        date = day.find('h1').string
        temp.append(date)
        # print(date)
        type = day.find_all('p')
        # print(type)
        temp.append(type[0].string)
        if type[1].find('span') is None:
            high = None
        else:
            high = type[1].find('span').string
            high = high.replace('℃', '')
        low = type[1].find('i').string
        low = low.replace('℃', '')
        temp.append(high)
        temp.append(low)
        # print(low)
        findall_dict[date] = temp
    # print(temp)
    # for date, value in findall_dict.items():
    #     print(value, end="\n")
    return findall_dict


xian = KnowWeather(url='http://www.weather.com.cn/weather/101110101.shtml')  # 西安
baoji = KnowWeather(url='http://www.weather.com.cn/weather/101110901.shtml')  # 宝鸡
ankang = KnowWeather(url='http://www.weather.com.cn/weather/101110701.shtml')  # 安康
xianyang = KnowWeather(url='http://www.weather.com.cn/weather/101110200.shtml')  # 咸阳

for date, value in baoji.items():
    print(value, end='\n')
