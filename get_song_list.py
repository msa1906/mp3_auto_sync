import requests
import re
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import math
import socket  
import time  
from pydub import AudioSegment
import re
import pafy
import os
import threading

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

playList = []
directory = r'C:\Users\Logan\Desktop\mp3_auto_sync'
for filename in os.listdir(directory):
	if filename.endswith(".mp3") or filename.endswith('.webm'):
		playList.append(filename)
def download_change_format(ele):
	name = ele.get_text().strip()
	url ='https://www.youtube.com' + ele['href']
	video = pafy.new(url)
	bestaudio = video.getbestaudio()
	format = re.search('audio:(.*)@.*',str(bestaudio))
	format = format.group(1)
	filename = video.title.strip()
	if str(filename +'.mp3') in playList or str(filename +'.webm') in playList:
		print(filename + 'is already download')
		return
	for i in range(2):
		try:
			bestaudio.download()
			break
		except:
			print(filename + 'download error')
			continue
			
	for i in range(2):
		try:
			other = AudioSegment.from_file(filename +'.' + format, format)
			break
		except:
			print(filename + 'read format error')
			time.sleep(1)
			continue
	for i in range(2):
		try:
			other.export(filename + '.mp3', format = 'mp3')
			print('finish ' + filename)
			break
		except:
			print(filename + 'exprot error')
			continue
	for i in range(2):
		try:
			os.remove(filename +'.' + format)
			break
		except:
			print(filename + 'remove error')
			continue
	

for ele in count_group:
	download_change_format(ele)

#change rest
for filename in os.listdir(directory):
	if filename.endswith(".webm"):
		try:
			other = AudioSegment.from_file(filename , format)
			for i in range(2):
				try:
					other.export(filename[:-5] + '.mp3', format = 'mp3')	
					os.remove(filename)
					break
				except:
					print(filename + 'second time change format error')
					continue
		except:
			pass
	elif filename.endswith('.temp'):
		os.remove(filename);