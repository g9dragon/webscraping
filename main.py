import requests
from bs4 import BeautifulSoup
req=requests.get("https://vnexpress.net/giao-duc")
soup=BeautifulSoup(req.text,"html.parser")

import getpagecontent

import json
import os
import sys

#Database

fh=open("ScrapedData.js",'w',encoding='utf-8')
###first Article
fct=[]
article=getpagecontent.getcontent(soup.h1.a['href'])
#y=json.dumps(article).encode('utf8')

#another

for sfa in soup.find_all('li'):
	if (sfa.h4):
		if ((sfa.a['href'].startswith('http'))&('longform' not in sfa.a['href'])&('video' not in sfa.a['href'])):
#                        if ('longfrom' in sfa.a['href']): sfa=next(soup.find_all('li'))
			article=getpagecontent.getcontent(sfa.a['href'])
			fct.append(article)
			#SaveFileOnComputer
			fh.write(str(fct))
fh.close()

#SaveFileToMongo
import Mongodb
Mongodb.savefile(fct)
