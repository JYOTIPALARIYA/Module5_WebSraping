import requests            #To Obtain the information we use requests
from bs4 import BeautifulSoup   #to parse that information we ue beautiful soup and with the help of beautifulsoup we
import time                              #can target different links to extract Information

urls=["https://finance.yahoo.com/quote/GOOGL?p=GOOGL&.tsrc=fin-srch&guccounter=1","https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch"]
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}


for url in urls:
    html_page=requests.get(url,headers=header)#now again and again if we try to fetch data from the site then it will understand that
                                #its a bot so will use header element and in that my user agent.
    # print(html_page)
    # now will create soup obj and pass html page content and parser ..here we r passing lxml which is fastest.
    soup=BeautifulSoup(html_page.content,'lxml')#we can know abt parsers through beautiful soup documentation.
    print(soup.title)#not a good one so can use find method
    headerin=soup.find_all("div",id="quote-header-info")[0]
    soup_title=headerin.find("h1",class_="D(ib) Fz(18px)").get_text()
    print(soup_title)


    soup_value=headerin.find("div",class_="D(ib) Mend(20px)").find("span").get_text()
    print(soup_value)
    soup_tablev=soup.find_all("div",class_="D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)")[0].find_all("tr")


    # previousCloseHeading=soup_tablev[0].find_all("span")[0].getText()
    # previousCloseValue=soup_tablev[1].find_all("span")[1].getText()
    # print(previousCloseHeading +" "+previousCloseValue)

    #-------------------now using for Loop
    for i in range(0,8):

        Heading=soup_tablev[i].find_all("td")[0].getText()
        Value=soup_tablev[i].find_all("td")[1].getText()
        print(Heading +" "+Value)
    time.sleep(5)