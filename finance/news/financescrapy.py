import urllib.request
import re

def getHtml(url):
    page = urllib.request.urlopen(url)
    ht = page.read()
    ht = ht.decode('utf-8')
    return ht

def getHttp(ht):
     reg=r'href="(.+?\d{7}\.html)" target=\"\_blank\"'
     hrefre=re.compile(reg)
     hreflist=re.findall(hrefre,ht)
     hreflist=sorted(set(hreflist),key=hreflist.index)
     return hreflist

def getTime(hreflist):
     Timelist=[]
     for ab in hreflist:
          x=getHtml(ab)
          Time=r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}'
          Timere=re.compile(Time)
          TI=re.findall(Timere,x)
          for o in TI:Timelist.append(o)
     return Timelist
               

def getTittle(href):
          x=getHtml(href)
          Tittle=r'<h1 class="f-ff1 f-fwn f-fs30">(.*)<\/h1>'
          Tittlere=re.compile(Tittle)
          TI=re.findall(Tittlere,x)
          return TI

     

hl = getHtml("http://www.yicai.com/news/finance/")
ad=getHttp(hl)
tl=getTime(ad)






