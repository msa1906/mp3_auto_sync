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
url = 'https://www.youtube.com/playlist?list=PLyUT0JApKHiPob4_PkY55yp4C5weNmLYO'

filename = 'current'

page_num = 1

page = requests.get(url)
	
soup = BeautifulSoup(page.text, 'html.parser')

count_group =  soup.select('div a.pl-video-title-link')
list_name = 'pop'



playList = []
directory = os.path.dirname(os.path.realpath('__file__'))
newfilder = directory + '\\' + list_name.replace('\\','').replace('.','')
if not os.path.exists(newfilder):
	print('try to create folder')
	directory = newfilder
	os.makedirs(list_name)
os.chdir(directory)
for filename in os.listdir(directory):
	if filename.endswith(".mp3") or filename.endswith('.webm'):
		playList.append(filename)
def download_change_format(ele):
	name = ele.get_text().strip()
	url ='https://www.youtube.com' + ele['href']
	try:
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
	except:
		print('forbiden video')

for ele in count_group:
	download_change_format(ele)

#change rest
for filename in os.listdir(directory):
	if filename.endswith(".webm"):
		print(filename + '  changing')
		try:
			other = AudioSegment.from_file(filename , 'webm')
			for i in range(2):
				try:
					other.export(filename[:-5] + '.mp3', format = 'mp3')	
					break
				except:
					print(filename + 'second time change format error')
					continue
		except MemoryError:
			print('MemoryError in audiosegment')
			
		os.remove(filename)
	elif filename.endswith('.temp'):
		os.remove(filename);