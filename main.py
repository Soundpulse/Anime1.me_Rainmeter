from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


req = Request('http://anime1.me/', headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(urlopen(req).read(), features="lxml")

text_file = open("input.txt", "r")
wishlist = text_file.read().split('\n')

names, status, links = [], [], []

section = soup.find_all('tr')

# Get every anime on the first page
for count in range(1, 20):
    columns = section[count].find_all('td')
    link = 'http://anime1.me' + columns[0].find('a').get('href')
    name = columns[0].get_text()
    stat = columns[1].get_text()
    names.append(name)
    status.append(stat)
    links.append(link)

# Write to txt
text_file = open("output.txt", "w")

print("新番列表:")
text_file.write("新番列表:\n")

for item in names:
    for item2 in wishlist:
        if (item2 in item) and (item2 != ""):
            name = item
            stat = status[names.index(item)]
            link = links[names.index(item)]

            # Retrieve Video
            req_inner = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
            soup_inner = BeautifulSoup(urlopen(req_inner).read(), features="lxml")
            vid = soup_inner.find('article').find('iframe').get('src')
            # Write to file
            text_file.write(name + "\n" + stat + "\n" + vid + "\n")
            print(name)
            print(stat)
            print(vid)

text_file.close()
