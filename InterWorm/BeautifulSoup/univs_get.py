#:ecoding=utf-8
import requests
from bs4 import BeautifulSoup
import bs4
def getHTMLText(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[3].string])

def printUnivList0(ulist,num):
    print "{:^10}\t{:^6}\t{:^10}".format("排名","学校名称","总分")
    for i in range(num):
        u=ulist[i]
        print "{:^10}\t{:^6}\t{:^10}".format(u[0].encode('utf-8'),u[1].encode('utf-8'),u[2])

def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(32)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1].encode('utf-8'),u[2],chr(32)))

def main():
    uinfo=[]
    url="http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html"
    html=getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)
    
main()
