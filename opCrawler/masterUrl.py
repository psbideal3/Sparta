import time

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

from selenium import webdriver


from bs4 import BeautifulSoup

@app.route('/')
def home():
    return 'This is Home!'

@app.route('/mypage')
def mypage():
    return render_template('mainPage.html')

@app.route('/masterInfo')
def masterInfo():
    return render_template('masterInfo.html')

@app.route('/searchMaster')
def search():
    championReceive = request.args.get('champName')
    result = scrapping(championReceive)
    return jsonify({'result': 'success', 'showResult' : result})

def scrapping(champReceive):
    result = []
    driver = webdriver.Chrome('C:\chromedriver_32\chromedriver')
    urlChampion = 'https://www.op.gg/ranking/champions/name=' + champReceive
    driver.get(urlChampion)
    time.sleep(1)
    req = driver.page_source

    # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
    soup = BeautifulSoup(req, 'html.parser')

    ranker1To3 = soup.select("#ChampionRankingUpdateArea > div > div.ranking-summary-summoner > div")
    ranker4To50 = soup.select("#ChampionRankingUpdateArea > div > table > tbody > tr")
    rank = 1
    for AA in ranker1To3:
        ranker_tag = AA.select_one("a > div")
        if ranker_tag is not None:
            ranker = ranker_tag.text
            print(ranker)
            result.append(ranker)


    for BB in ranker4To50:
        ranker_tag = BB.select_one("td > a")
        if ranker_tag is not None:
            ranker = ranker_tag.text
            print(ranker)
            result.append(ranker)
    print(result[0])
    driver.close()
    return result


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
