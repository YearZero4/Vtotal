import requests, time, json, pandas, re
import numpy as np

def vtotal(url):
 api_key = "5ccc5ed7c1decdfc3b81dbf8a844d62ac71bebc348e83806d1898583412b16c7"
 params = {'apikey': api_key, 'resource': url}
 response = requests.get("https://www.virustotal.com/vtapi/v2/url/report", params=params)
 n=1
 number=[]

 if response.status_code == 200:
  result = response.json()
  i=result
  i=str(i)
  res=i.replace(',', '\n').replace('{', '').replace('}', '').replace('\'', '')
  ss=res.splitlines()
  for d in ss:
   d=d.strip()
   find1=re.search('positives:', d)
   find2=re.search('True', d)
   if find1 != None:
    result=d.split()[1]
    result=int(result)
    if result == 0:
     print("Pagina Web Segura")
    else:
     print("Pagina Web Insegura")
   if find2 != None:
    print(d)
    number.append(n)
   if number:
    linea=number[0]+1
    if n == linea:
     print(d)
     number.clear()
   n=n+1
print("")
url=input("URL QUE DESEA VERIFICAR -> ")
print("")
vtotal(url)
