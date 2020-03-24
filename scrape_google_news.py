import pandas as pd
import numpy as np
import requests
from newspaper import Article
import json
from bs4 import BeautifulSoup
from newspaper import Article

#The following is a function to search for exact keywords and print the corresponding sentences in an original text of the article

def search_keyword(word,para):
    for sentence in para.split('.'):
        if word in sentence:
            print(sentence)


base_url = "http://news.google.com"

print("Hi! I am gonna show you the latest news.") 
print("Fetching headline...")
#pull the main headlines
response = requests.get(base_url)
htmlcontent = response.content
main_soup=BeautifulSoup(htmlcontent, 'html.parser')
main_articles = main_soup.select('article a')

n=1
index=0
article_titles=[]
article_text=""
article_summaries=[]
article_dates=[]
article_urls=[]
while(n!=0 and index< len(main_articles)):
    
    try:
        print(base_url+main_articles[index]['href'].strip('.'))
        index=index+1
    except KeyError:
        continue
    #We now parse the article
 
    try:

        article=Article(base_url+main_articles[index]['href'].strip('.'),language='en')
    except KeyError:
        continue
    article.download()
    article.parse()
    article_text=article.text
    try:
        article_urls.append(base_url+main_articles[index]['href'].strip('.'))
    except KeyError:
        pass
    article_titles.append( article.title)
    article_dates.append(article.publish_date)
    article.nlp()
    article_summaries.append(article.summary)

    data = {'Title':article_titles, 'Summary':article_summaries, 'Date':article_dates, 'URL': article_urls}

    df =pd.DataFrame.from_dict(data)
    print(df)    
    

    print("Enter Y to search specific keywords: ",end=" ")
    if(input())=='Y':
        print("Enter words: ")
        words = input().split(" ")
        for word in words:
            search_keyword(word,article_text)
    
   
    
    print("\nDo you want more news? (Enter 1 or 0): ", end=" ")
    n=int(input())

print("\nThankyou!")