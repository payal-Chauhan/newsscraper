import pandas as pd
import numpy as np
import requests
from newspaper import Article
import json
from bs4 import BeautifulSoup

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
while(n!=0 and n< len(main_articles)):
    
    try:
        print(main_articles[index]['href'])
        index=index+1
    except KeyError:
        pass
    
   
    
    print("\nDo you want more news? : ", end=" ")
    n=int(input())

print("\nThankyou!")