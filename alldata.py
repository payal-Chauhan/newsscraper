import pandas as pd
import numpy as np
import requests
from newspaper import Article
import json
from bs4 import BeautifulSoup




base_url = "http://news.google.com"

response1 = requests.get(base_url)
all_news = response1.content
soup1 = BeautifulSoup(all_news, 'html.parser')
links = soup1.select('h3 a')

#Now extract the link from anchor elements and visit the link
# 
# 
news_links = []
j=0
for i in links:
   news_links.append( i['href'])

# processing only the first link we have in our Dataset
news_links[0] = base_url+news_links[1].strip('.')

news = Article(news_links[0],language='en')
news.download()
news.parse()
news.nlp()
#now we have the attributes  title, summary, and url
#we will make a json file out of them
titles = []
summary=[]
titles.append(news.title)
summary.append(news.summary)
record= {"title": titles, "summary":summary}
myjson = json.dumps(record)
df = pd.DataFrame.from_dict(record)
print(df.head(n))

# wrap it up in a loop later

