
from bs4 import BeautifulSoup
import requests
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import time
import platform
import numpy as np
from PIL import Image
import csv


url = 'https://www.midjourney.com/jobs/b43f95f1-7e89-42cd-a02f-8a3880f0830c?index=0'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
midjourney = soup.find_all('div')

print(midjourney)
