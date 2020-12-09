import requests            #To Obtain the information we use requests
from bs4 import BeautifulSoup   #to parse that information we ue beautiful soup and with the help of beautifulsoup we
                                #can target different links to extract Information
url="https://finance.yahoo.com/quote/GOOGL?p=GOOGL&.tsrc=fin-srch&guccounter=1"
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}

html_page=requests.get(url)#now again and again if we try to fetch data from the site then it will understand that
                            #its a bot so will use header element and in that my user agent.
# print(html_page)
# now will create soup obj and pass html page content and parser ..here we r passing lxml which is fastest.
soup=BeautifulSoup(html_page.content,'lxml')#we can know abt parsers through beautiful soup documentation.
print(soup.title)#not a good one so can use find method
title=soup.find('title').getText()
print(title)