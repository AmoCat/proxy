import urllib
import socket
import re
import urllib2
from urllib2 import Request
from bs4 import BeautifulSoup
import sys
import json

socket.setdefaulttimeout(3)
f = open("proxy.txt")
out = open("available_ip.txt","w")
lines = f.readlines()
proxys = []
for i in range(0,len(lines)):
    ip = lines[i].strip("\n").split("\t")
    proxy_host = "http://"+ip[0]+":"+ip[1]
    proxy_temp = {"http":proxy_host}
    proxys.append(proxy_temp)
    url = "http://ip.chinaz.com/getip.aspx"
for proxy in proxys:
    try:
        res = urllib.urlopen(url,proxies=proxy).read()
        res = re.sub(r"(,?)(\w+?)\s*?:", r"\1'\2':", res);
        res = res.replace("'","\"")
        js = json.loads(res)
        print js['ip']
        #out.write(js['ip']+"\n")
        #out.flush()
    except Exception,e:
        print proxy
        print e
        continue
f.close()
out.close()
