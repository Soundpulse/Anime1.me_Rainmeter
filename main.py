from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


req = Request('http://anime1.me/', headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(urlopen(req).read(), features="lxml")

text_file = open("input.txt", "r")
wishlist = text_file.read().split('\n')

names, status, links = [], [], []

section = soup.find_all('tr')
for count in range(1, 10):
    columns = section[count].find_all('td')
    link = 'http://anime1.me' + columns[0].find('a').get('href')
    name = columns[0].get_text()
    stat = columns[1].get_text()
    names.append(name)
    status.append(stat)
    links.append(link)

# Write to txt
text_file = open("output.txt", "w")

print("今日新番:")
text_file.write("今日新番:\n")
# for item in names:
#     text_file.write("   " + item + "\n")
#     print("   " + item)

for item in wishlist:
    for item2 in names:
        if item in item2:
            name = item2
            stat = status[names.index(item2)]
            link = links[names.index(item2)]
            text_file.write(name + "\n" + stat + "\n" + link + "\n")
            print(name)
            print(link)


text_file.close()
