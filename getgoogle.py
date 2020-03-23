import requests
from bs4 import BeautifulSoup

#getting the first response from google news
base_url = "http://news.google.com"

response1 = requests.get(base_url)
all_news = response1.content
soup1 = BeautifulSoup(all_news, 'html.parser')
links = soup1.find_all('a',class_='VDXfz')

#Now extract the link from anchor elements and visit the link
# 
# 
news_links = []
j=0
for i in links:
   news_links.append( i['href'])


for i in news_links:
    actual_url = base_url+ i.strip('.')
    #now we visit this particular news url

    response2 = requests.get(actual_url).text
    soup2 = BeautifulSoup(response2, 'html.parser')
    headlines = soup2.find_all('h1')
    for x in headlines:
        print(x.text)



