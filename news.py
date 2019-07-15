import requests
from bs4 import BeautifulSoup
url = "https://news.naver.com"

req = requests.get(url)
html = req.text
soup = BeautifulSoup(html,'html.parser')
rankStr = "#ranking_10"
print(soup)
for i in range(0,6):    
    rankList = soup.select(rankStr+str(i))
    print(rankList)
    aList = []
    for rank in rankList:
        aList = rank.find_all('a')

        with open("news.txt","a") as f:
            f.write("#####"+str(i)+"####\n")
            for article in aList:
                f.write(article.text + "\n" + url +article['href'] +"\n\n")
            f.write("###################\n")
