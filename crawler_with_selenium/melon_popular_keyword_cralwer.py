# https://www.melon.com/search/trend/index.htm
# 최근 10일간 인기 키워드 리스트 확인

import time
import selenium
from selenium import webdriver

URL = 'https://www.melon.com/search/trend/index.htm'

#options = webdriver.ChromeOptions()
#options.add_argument('headless')

driver = webdriver.Chrome(executable_path='./chromedriver.exe')#, options=options)

driver.get(url=URL)

for day in range(10) :
    keyword_list_div=driver.find_elements_by_class_name("wrap_list_keywd")
    #print(len(keyword_list_div))

    date=keyword_list_div[0].find_element_by_class_name("no").text
    print("--", f"date : {date}", "--")

    prev_button=keyword_list_div[0].find_element_by_class_name("pre")

    keyword_list_div_row_list=keyword_list_div[0].find_elements_by_class_name("keywd_rank")
    #print(len(keyword_list_div_row_list))
    for keyword_list_div_row in keyword_list_div_row_list:
        rank=keyword_list_div_row.find_element_by_class_name("rank").text
        keyword = keyword_list_div_row.find_element_by_class_name("keywd").text
        print("\t", rank+" - "+keyword)
    print("----")
    print("")

    prev_button.click()
    time.sleep(3)

time.sleep(3)

driver.close()