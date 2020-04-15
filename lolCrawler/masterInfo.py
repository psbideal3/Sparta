from selenium import webdriver
driver = webdriver.Chrome('C:\\Users\\82108\\Desktop')

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

from bs4 import BeautifulSoup

url = 'https://www.op.gg/ranking/champions/name=fiddlesticks'
driver.get(url)
req = driver.page_source

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(req, 'html.parser')

ranker1To3 = soup.select("#ChampionRankingUpdateArea > div.champion-ranking > div.ranking-summary-summoner > div")
rank = 1
for AA in ranker1To3:
     print("22")
     ranker_tag = AA.select_one("a > div")
     if ranker_tag is not None:
         ranker = ranker_tag.text;
         tier = ranker1To3.select_one("div.ranking-summary-summoner__tierlevel > b")

         info1To3 = {
             'rank': rank,
             'ranker': ranker,
             'tier': tier
         }
         db.ranker1To3.insert_one(info1To3)




