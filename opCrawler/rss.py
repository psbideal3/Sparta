import time
import requests

from pymongo import MongoClient
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
time.sleep(1)
data = requests.get('https://www.op.gg/ranking/champions/name=fiddlesticks', headers=headers)
time.sleep(1)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')
time.sleep(1)

ranker1To3 = soup.select("#ChampionRankingUpdateArea > div > div.ranking-summary-summoner > div")
ranker4To50 = soup.select("#ChampionRankingUpdateArea > div > table > tbody > tr")
rank = 1
for AA in ranker1To3:
    ranker_tag = AA.select_one("a > div")
    if ranker_tag is not None:
        ranker = ranker_tag.text

for BB in ranker4To50:
    ranker_tag = BB.select_one("td > a")
    if ranker_tag is not None:
        ranker = ranker_tag.text
        print(ranker)
