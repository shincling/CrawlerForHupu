__author__ = 'shin'
import urllib2
import re
import time
from scrapy.spider import BaseSpider

from shinnn.items import ShinnnItem




class HupuSpider(BaseSpider):
   name = "shin_hupu"
   allowed_domains=['hupu.com']
   start_urls = [
       "http://bbs.hupu.com/vote"
       #"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
   ]

   def parse(self, response):
       page=urllib2.urlopen(response.url).read()

       lists=re.findall(r'''href="/([0-9]*).html">(.*)</a>''',page)
       items=[]
       for list in lists:
           item=ShinnnItem()
           item['link']=r"http://bbs.hupu.com/"+list[0]+"html"
           item['title']=list[1]
           tiezi=urllib2.urlopen(item['link']).read()
           time.sleep(3)
           tiezi=tiezi.split('w_reply clearfix')[-1]
           tiezi=tiezi.split('w_reply clearfix')[0]
           highlights_num=re.findall(r'\(<span class="stime">([0-9]*)',tiezi)
           highlights_words=re.findall(r'<tr><td>\n\n(.*)\n\n',tiezi)
           assert len(highlights_num)==len(highlights_words)
           for word in highlights_words:
               item['content']=word
           for num in highlights_num:
               item['number']=num

           items.append(item)
           #print item

       return items


