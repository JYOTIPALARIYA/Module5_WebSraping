import requests            #To Obtain the information we use requests
from bs4 import BeautifulSoup   #to parse that information we ue beautiful soup and with the help of beautifulsoup we
                                #can target different links to extract Information
url="https://en.wikipedia.org/wiki/Python_(programming_language)#References"

html_page=requests.get(url)
soup=BeautifulSoup(html_page.content,'lxml')#we can know abt parsers through beautiful soup documentation.

cont=soup.find("div",class_="reflist columns references-column-width")
#-------------------now using for Loop
for i in range(0,186):
    c=cont.find_all("li")[i].text
    print(i+1,c)


  