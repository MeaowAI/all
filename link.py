import requests
from bs4 import BeautifulSoup
import numpy as np
from manageFile import ManageFile


a = requests.get("https://www.w3schools.com/python/default.asp")
soup = BeautifulSoup(a.content, 'html.parser')

s = soup.get_text().split()
d = {}
for x in s:
    if x not in d.keys():
        d[x]=1
    else:
        d[x]=d[x]+1


strdat =""
for key, value in sorted(d.items(), key = lambda kv:(kv[1], kv[0]),reverse=True):
    if value != 1:
        strdat = strdat + key + " >>> " +value.__str__()+"\n"


ManageFile().writeText("t.txt","w",strdat)
