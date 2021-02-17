import urllib.request
import xml.etree.ElementTree as ET

url = 'https://www.yahoo.com/news/rss'
url = 'http://feeds.marketwatch.com/marketwatch/topstories/'

with urllib.request.urlopen(url) as response:
   data = response.read()
   root = ET.fromstring(data)
   channel = root[0]
   for news_title in channel.iter('title'):
       print(news_title.text + '\n')