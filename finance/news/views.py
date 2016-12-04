from django.shortcuts import render
from django.http import HttpResponse
from .financescrapy import getHttp,getHtml,getTime,getTittle

hl = getHtml("http://www.yicai.com/news/finance/")
ad=getHttp(hl)
tl=getTime(ad)

combine=dict(map(lambda x,y:[x,y],ad,tl))
dic={}
for key in ad:
	dic[getTittle(key)[0]]={key:combine[key]}
    


                           
# Create your views here.
def home(request):
	
	return render(request,'index.html',{'dic':dic})
