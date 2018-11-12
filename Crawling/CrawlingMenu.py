from bs4 import BeautifulSoup
import requests
import csv
import urllib

f = open('nowon.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
dataset = []
for line in rdr:
    dataset.append([line[0],line[1]])
del(dataset[0])
f.close()
menu = []
count = 0
print(dataset)

f2 = open('output.csv', 'w', encoding='euc_kr', newline='')
wr = csv.writer(f2)

for a in dataset:
    try:
        keyword = a[0]+" "+a[1]
        key_url = urllib.parse.quote(keyword.encode('utf-8'))

        url = "https://m.search.daum.net/search?w=tot&nil_mtopsearch=reckwd&DA=BJE&q={}".format(keyword)
        headers = {"User-Agent": "User-Agent:Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        html_text = response.text
        soup = BeautifulSoup(html_text, 'html.parser')
        crawl_one = soup.find("ul", {"class":"list_place"}).findAll("a")
        sec_url = str
        for b in range(1):
            sec_url = crawl_one[b].get("href")
        url2 = "https://m.search.daum.net/search"+sec_url
        response2 = requests.get(url2, headers=headers)
        html_text2 = response2.text
        soup2 = BeautifulSoup(html_text2, 'html.parser')
        categorys = soup2.find("div", {"class": "head_cont"}).findAll("span", {"class": "txt_info"})
        for c in categorys:
            category = c.get_text()
            menu.append(category)
        if category[-1] == ",":
            category = category[:-1]
        count += 1
        print(count)
        category = category.replace(u'\xa0', ' ')
        wr.writerow([category])

    except:
        menu.append("없음")
        count += 1
        print(count)
        wr.writerow(["없음"])

f.close()