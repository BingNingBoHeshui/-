# _*_coding : utf-8 _*_
# @Time : 2024/11/27 17:15
# @Author : 刘佳琳
# @File : lishitianqi
# @Project : pythonProject2
import csv  # 写入csv文件
import time  #休眠
from selenium import webdriver  #网页交互
from selenium.webdriver.common.by import By #定位网页元素

import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie ,Bar,Timeline

browser=webdriver.Chrome() #浏览器驱动
def get_mes():
    weather = []
    for month in range(1, 13):
        dayTime = f'2023{month:02}'
        url = f'https://lishi.tianqi.com/chongqing/{dayTime}.html'
        browser.get(url)
        time.sleep(1)
        button = browser.find_element(By.CLASS_NAME, 'lishidesc2') #定位“查看更多”
        button.click() #点击
        time.sleep(1)
        element = browser.find_element(By.CLASS_NAME, 'thrui').text
        month_weather = element.split()  # 根据空白符分割字符串
        for i in range(0, len(month_weather)):
            if i % 7 == 0:
                day_weather = {
                    'date_time': month_weather[i],
                    'week':  month_weather[i + 1],
                    'hight': month_weather[i + 2],
                    'low': month_weather[i + 3],
                    'weather': month_weather[i + 4],
                    'wind': month_weather[i + 5],
                    'level': month_weather[i + 6]
                }
                weather.append(day_weather)
    return weather

weather=get_mes()
browser.quit()
csvfile=open("weather.csv", "w", newline='')
writer = csv.writer(csvfile)
writer.writerow(["日期", "星期", "最高气温", "最低气温", '天气', "风向", "风级"])  # 先写入列名:columns_name
for day_weather_dict in weather:  # 遍历出每个月的天气信息
    writer.writerow(list(day_weather_dict.values()))  # 将每天的天气信息写入csv文件