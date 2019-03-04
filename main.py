from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

req = Request('http://anime1.me/', headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(urlopen(req).read())

wishlist = ['史萊姆']
names, status, link = [], [], []

section = soup.find_all('tr')
for count in range(1, 10):
    columns = section[count].find_all('td')
    link = 'http://anime1.me' + columns[0].find('a').get('href')
    name = columns[0].get_text()
    stat = columns[1].get_text()
    names.append(name)
    status.append(stat)

print("今日新番:")
for item in names:
    print("   " + item)

print("\n==============================")
for item in wishlist:
    for item2 in names:
        if item2.find(item) != -1:
            print("最新一集嘅'" + item2 + "'已經出咗!")
print("==============================")
