# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import json

User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent

url_origin = 'http://www.xicidaili.com/nn/'
f = open("proxy.txt","w")
for i in range(1,10):
	url = url_origin + str(i)
	req = urllib2.Request(url,headers=header)
	res = urllib2.urlopen(req).read()

	soup = BeautifulSoup(res,'html.parser')
	ips = soup.findAll('tr')

	for x in range(1,len(ips)):
		ip = ips[x]
		#f.write(ip.encode('utf-8'))
		tds = ip.findAll("td")
		ip_temp = tds[1].contents[0]+"\t"+tds[2].contents[0]+"\n"
		# print tds[2].contents[0]+"\t"+tds[3].contents[0]
		f.write(ip_temp.encode('utf-8'))
