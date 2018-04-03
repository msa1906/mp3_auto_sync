import requests
import re
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import math
import socket  
import time  
  
  
def ensureUtf(s):
  try:
      if type(s) == unicode:
        return s.encode('utf8', 'ignore')
  except: 
    return str(s)
	
socket.setdefaulttimeout(20)
url = 'https://www.youtube.com/playlist?list=PLOE6peTePk0mMA0P6QNkuHxkZTcmuzZwu'

filename = 'current'

page_num = 1

page = requests.get(url)
	
soup = BeautifulSoup(page.text, 'html.parser')

count_group =  soup.select('div a.pl-video-title-link')

for ele in count_group:
	name = ele.get_text().strip()
	url ='https://www.youtube.com' + ele['href']

	with open(filename+'.csv', 'a', newline='', encoding='utf-8') as csvfile:
		spamwriter = csv.writer(csvfile)
		list1 = [name, url]
		list1 = list(map(lambda x:ensureUtf(x), list1))
		print(list1)
		spamwriter.writerow(list1)