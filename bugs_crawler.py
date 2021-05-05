# 여기에서 부터 최초로 학생1이 파일을 생성했고 코딩하기 시작합니다.
from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20210504&charthour=21")

soup=BeautifulSoup(html, "lxml")
#print(soup)

song_chart_table = soup.find_all('table', {"class":"byChart"})
#print(song_chart_table)
#print(len(song_chart_table))

song_chart_table_tbody= song_chart_table[0].find_all("tbody")
#print(song_chart_table_tbody)
#print(len(song_chart_table_tbody))

song_chart_table_tbody_row=song_chart_table_tbody[0].find_all("tr")

real_time_song_ranking=dict()
for song_row in song_chart_table_tbody_row :
    # 랭킹 순위 수집
    ranking_div=song_row.find_all("div",{"class":"ranking"})
    ranking_strong=ranking_div[0].find_all("strong")
    ranking_text=ranking_strong[0].get_text()
    #print(ranking_text)

    # 제목 수집
    title_p = song_row.find_all("p", {"class": "title"})
    title_text=title_p[0].get_text()
    #print(title_text.strip())

    real_time_song_ranking[ranking_text]=title_text.strip()

print("-- 2021-05-04 벅스뮤직 실시간 음원 차트 --")
for ranking, title in real_time_song_ranking.items():
    print(f"\t{int(ranking):3d} - {title}")

# 여기 까지 학생1이 코드를 작성하고 실행한 다음 스크린캡처합니다. 그리고 git 온라인 저장소에 업로드 합니다.