#Scrape data on VNEXPRESS
#BeautifulSoup
import getcmt
import requests
import urllib.request
import json
from bs4 import BeautifulSoup
def getcontent(pageurl):
    preq=requests.get(pageurl)
    psoup=BeautifulSoup(preq.text,"html.parser")
    #Title&content
    particle={'title':'','content':'','comment':[]}
    particle['title']=psoup.h1.text.strip()
    #print(particle['title'])
    particle['content']=psoup.p.text.strip()
    for ctn in psoup.article.find_all('p',{"class":"Normal"}):
        particle['content']+=ctn.text.strip()
    #Search for Call CmtFile Cmd
    h=str(psoup.find_all('div',{"id":"box_comment_vne"}))
    bstr=h.find('"article_id"')
    estr=h.find(',"limit"')
    #Transform CmtFile URL
    myurl='https://usi-saas.vnexpress.net/index/get?callback=jQuery&offset=0&'+h[bstr:estr].replace("article","object").replace("_","").replace('"','').replace(':','=').replace(',','&')
    jsfile=urllib.request.urlopen(myurl)
    jsfct=jsfile.read().decode('utf8').replace(');','').replace("/**/ typeof jQuery === 'function' && jQuery(","")
    cmtd=[]
    particle['comment']=cmtd=getcmt.clcmt(jsfct,0,cmtd)
    return particle
    #for cmt in cmtd:
     #   print('\t',cmt)
