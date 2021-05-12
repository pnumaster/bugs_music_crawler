# https://www.weather.go.kr
# 테마날씨 -> 세계 날씨 -> 아시아 -> 대한민국 -> 부산

import matplotlib.pyplot as plt
import matplotlib
from urllib.request import urlopen
from bs4 import BeautifulSoup

#html=urlopen("https://worldweather.wmo.int/kr/city.html?cityId=336")
html=urlopen("https://www.weather.go.kr/w/theme/world-weather.do?continentCode=C01&countryCode=126&cityCode=336")

soup=BeautifulSoup(html, "lxml")
#print(soup)

#weather_table = soup.find_all('table')
weather_table = soup.find_all('table', {"id":"climate_table"})
#print(weather_table)
print(len(weather_table))
print(type(weather_table))
print(type(weather_table[0]))

#weather_table_tbody= weather_table.find_all("tbody")
weather_table_tbody=weather_table[0].find_all("tbody")
#print(weather_table_tbody)
#print(len(weather_table_tbody))

weather_table_tbody_row= weather_table_tbody[0].find_all("tr")
#print(weather_table_tbody_row)
#print(len(weather_table_tbody_row))

busan_temp_info=[]
for tr in weather_table_tbody_row:
    month_temp_info=[]
    td=tr.find_all("td")
    #print(td)
    #print(len(td))
    #print("")

    for content in td:
        print(content.get_text(), end=', ')
        month_temp_info.append(content.get_text())
    print("")
    busan_temp_info.append(month_temp_info)

print("")

month_list=[]
temp_low_list=[]
temp_high_list=[]
temp_precipitation=[]

for month_temp_info in busan_temp_info:
    #print(month_temp_info)
    month_list.append(month_temp_info[0])
    temp_low_list.append(float(month_temp_info[1]))
    temp_high_list.append(float(month_temp_info[2]))
    temp_precipitation.append(float(month_temp_info[3]))

print(month_list)
print(temp_low_list)
print(temp_high_list)
print(temp_precipitation)


matplotlib.rcParams["axes.unicode_minus"]=False
plt.rc('font', family='Malgun Gothic')


x=range(len(month_list))

fig, ax1 = plt.subplots()
ax1.set_title('월별기후자료')
ax1.plot(x, temp_high_list, '-o',color="red")
ax1.plot(x, temp_low_list, '-o',color="blue")
ax1.set_ylim(-10, 30)
ax1.set_ylabel('강수량')

ax2=ax1.twinx()
ax2.set_ylabel('강수량')
ax2.bar(x, temp_precipitation, color="gray")
ax2.set_ylim(0, 300)
ax2.set_xlabel('Year')
ax2.set_ylabel('기온')

ax1.set_zorder(ax2.get_zorder() + 10)
ax1.patch.set_visible(False)

ax1.set_xticks(x)
ax1.set_xticklabels(month_list)

plt.show()
