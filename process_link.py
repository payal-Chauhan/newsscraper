from newspaper import Article
import requests
from bs4 import BeautifulSoup


def search_keyword(word,para):
    for sentence in para.split('.'):
        if word in sentence:
            print(sentence)



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
news_links[0] = base_url+news_links[0].strip('.')
print(news_links[0])
news = Article(news_links[0],language='en')
news.download()
news.parse()
news.nlp()

article_text= news.text
print("#############")
print(article_text)
word = input("enter a keyword to be searched in the article: ")
search_keyword(word,article_text)


