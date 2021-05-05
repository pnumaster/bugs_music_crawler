# https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20210504&charthour=21
# 사실 이 코드는 실시간 음원차트를 가져오지는 않지만 2021-05-04일 오후 9시 음원 차트를 최신으로 취급하며
# 곡 순위 변동 추이는 해당 일자로 00시 부터 오후 9시 까지만 반영합니다.

# 여기에서 부터 최초로 학생1이 파일을 생성했고 코딩하기 시작합니다.
from urllib.request import urlopen
from bs4 import BeautifulSoup

import matplotlib.pyplot as plt # 학생2가 임포트했습니다.
import matplotlib # 학생2가 임포트했습니다.

from time import sleep # urlopen을 사용하는 것은 결국 브라우저 해당 페이지에 접속하는 것과 같다. #학생2 가 임포트
# 따라서 사람이 직접 브라우저에서 접속하는 것보다 컴퓨터가 urlopen을 사용한 프로그램이 짧은시간 안에 여러번 접속할 수 있으므로
# 짧은 시간 안에 여러 번 접속하는 것은 벅스뮤직 같은 웹 서버 입장에서는 '이상(Anomaly)' 탐지에 걸릴 수 있으므로 접속 차단될 수 있다.

html=urlopen("https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20210504&charthour=21")

soup=BeautifulSoup(html, "lxml") # html.parser를 이용할 수도 있다.
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


# 이제 부터는 학생2가 학생1이 작성한 파일에서 크롤러 프로그램을 발전시킵니다.
# 꼭 학생1이 작성한 코드 밑에서 시작할 필요 없으며 학생1이 작성한 코드를 수정해도 됩니다.
# 제일 위에 matplotlib 라이브러리를 추가했듯이....

print("---- End of List ----")
print("")
song_ranking=input("찾으시는 곡에 대한 현재 순위를 입력해주세요 > ")
song_to_find=real_time_song_ranking[song_ranking]

url_list_by_timeline=[]
for time in range(0,22) : ## 00시 부터 21시(오후 9시)까지
    url_list_by_timeline.append(f"https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20210504&charthour={time:02d}")
    sleep(2) # 만약의 이상탐지에 걸리는 것을 미연에 방지하기 위해 2+a 초 간의 간격을 두고 접속함.

song_ranking_fluctuation=dict()
song_ranking_fluctuation['title']=song_to_find
song_ranking_fluctuation['ranking_by_time']=dict()
time_count=0
for time_url in url_list_by_timeline :
    html = urlopen(time_url)

    soup = BeautifulSoup(html, "lxml")

    song_chart_table = soup.find_all('table', {"class": "byChart"})
    song_chart_table_tbody = song_chart_table[0].find_all("tbody")
    song_chart_table_tbody_row = song_chart_table_tbody[0].find_all("tr")

    for song_row in song_chart_table_tbody_row:
        title_p = song_row.find_all("p", {"class": "title"})
        title_text = title_p[0].get_text()
        if title_text.strip()==song_to_find:
            ranking_div = song_row.find_all("div", {"class": "ranking"})
            ranking_strong = ranking_div[0].find_all("strong")
            ranking_text = ranking_strong[0].get_text()
            #print(ranking_text)
            song_ranking_fluctuation['ranking_by_time'][f'{time_count:02d}']=ranking_text
            break
    if not f'{time_count:02d}' in song_ranking_fluctuation['ranking_by_time'].keys() : #만약 차트에서 검색되지 않았다면 100위
        song_ranking_fluctuation['ranking_by_time'][f'{time_count:02d}'] = "100"
    time_count += 1

print("["+song_ranking_fluctuation['title']+"]의 00시 부터 21시 까지 순위 변동사항 입니다. :")
time_line=[]
ranking_seq=[]
for time, ranking in song_ranking_fluctuation['ranking_by_time'].items() :
    print(time,"시 -",ranking,"위")
    time_line.append(time+"시")
    ranking_seq.append(int(ranking))

matplotlib.rcParams["axes.unicode_minus"]=False
plt.rc('font', family='Malgun Gothic')
x=range(22)
plt.rcParams["figure.figsize"] = (10,6)
plt.plot(x, ranking_seq, '-o',color="red")
plt.gca().invert_yaxis()
plt.xticks(x, time_line)
plt.title("["+song_ranking_fluctuation['title']+"]의 00시 부터 21시 까지 순위 변동사항")
plt.show()

# 여기까지 학생2가 작성하고 인풋에 입력할 수 있는 모습을 캡쳐, 그래프 캡쳐 한 뒤, git에 업로드