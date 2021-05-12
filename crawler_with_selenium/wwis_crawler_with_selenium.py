# https://worldweather.wmo.int/kr/city.html?cityId=336
# 홈 -> 아시아 -> 대한민국 -> 부산

#import matplotlib.pyplot as plt
#import matplotlib
#from urllib.request import urlopen
#from bs4 import BeautifulSoup

#html=urlopen("https://worldweather.wmo.int/kr/city.html?cityId=336")

#soup=BeautifulSoup(html, "lxml")

#weather_table = soup.find_all('table', {"class":"climateTable"})
#print(len(weather_table))

# 위 방법은 더이상 이 페이지에서 먹히지 않는다.
# 이는 브라우저에서 자바스크립트를 읽은 직후 html코드를 생성하기 때문
# 이를 위해 selenium을 사용한다.

import time
import selenium
from selenium import webdriver

URL = 'https://worldweather.wmo.int/kr/city.html?cityId=336'

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=options)

driver.get(url=URL)
weather_table=driver.find_elements_by_class_name("climateTable")
print(len(weather_table))

weather_table_tbody=weather_table[0].find_elements_by_tag_name("tbody")
print(len(weather_table_tbody))

weather_table_tbody_tr_list=weather_table_tbody[0].find_elements_by_tag_name("tr")
print(len(weather_table_tbody_tr_list))

for weather_table_tbody_tr in weather_table_tbody_tr_list :
    weather_table_tbody_tr_td_list=weather_table_tbody_tr.find_elements_by_tag_name("td")
    for weather_table_tbody_tr_td in weather_table_tbody_tr_td_list :
        print("\t", weather_table_tbody_tr_td.text ,end="\t|-|\t")
    print("")
time.sleep(3)

driver.close()