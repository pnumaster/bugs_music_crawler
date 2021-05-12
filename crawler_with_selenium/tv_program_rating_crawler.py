# https://www.naver.com/
# 티비 프로그램 시청률을 검색하는 크롤러

import time
import selenium
from selenium import webdriver

print("시청률이 궁금한 티비 프로그램 3개를 입력하시오(콤마로 구분할 것)")
print("ex : 나혼자 산다, 라디오 스타, 코미디빅리그")
program_list_string=input(">> : ")
program_list=program_list_string.split(",")

URL = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query='
driver = webdriver.Chrome(executable_path='./chromedriver.exe')#, options=options)
driver.get(url=URL)

for tv_program in program_list:
    search_box=driver.find_element_by_name("query")
    search_box.send_keys(tv_program)

    search_btn=driver.find_element_by_class_name("bt_search")
    search_btn.click()

    title= driver.find_element_by_class_name("title").text
    rating = driver.find_element_by_class_name("value").text

    print(title+" - "+rating)

    time.sleep(3)
    search_box = driver.find_element_by_name("query")
    search_box.clear()

time.sleep(3)

driver.close()