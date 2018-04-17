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

directory = r'C:\Users\Logan\Desktop\mp3_auto_sync'

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