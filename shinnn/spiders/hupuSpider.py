__author__ = 'shin'
import urllib2
import re
import time
from scrapy.spider import BaseSpider

from shinnn.items import ShinnnItem




class HupuSpider(BaseSpider):
   name = "shin_hupu"
   #allowed_domains=['hupu.com']
   start_urls = [
       "http://bbs.hupu.com/vote"
       #"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
   ]

   def parse(self, response):
       page=urllib2.urlopen(response.url).read()


       lists=re.findall(r'''href="/([0-9]*).html">(.*)</a>''',page)

       items=[]
       f=open(r'e:\test\hupu.txt','w')
       for list in lists[0:5]:


           link=r"http://bbs.hupu.com/"+list[0]+".html"
           tiezi=urllib2.urlopen(link).read()
           time.sleep(2)
           print '\n\ncccccccc\n\n'
           if tiezi.find('w_reply clearfix')!=-1:
               tiezi=tiezi.split('w_reply clearfix')[-1]
               tiezi=tiezi.split(r'/vote/highlights')[0]




               #assert len(highlights_num)==len(highlights_words)
               highlights_num=re.findall(r'''\(<span class="stime">([0-9]*)''',tiezi)
               print "\n\nnum:\n\n"
               print highlights_num
               ##highlights_words=re.findall(r'''<tr><td>\n\n.*\n\n</td>|<tr><td>\n\n[^/]*\n\n</td>''',tiezi)
               highlights_words=re.findall(r'''<td>\n\n((?:\n|.)*?)\n\n</td>''',tiezi)# shishangzuijia!

               print '\n\n\hhhhhhh\n\n\n'



               highlights_words=re.findall(r'''<td>\n\n((?:\n|.)*?)\n\n</td>''',tiezi)# shishangzuijia!
               #print '\n\n\n\n\n'+tiezi+'\n\n\n\n\n\n'

               highlights_words=re.findall(r'''<tr><td>\r\n((?:\n|.)*?)\r\n</td>''',tiezi)
               print '\n\nwords:\n\n'
               print highlights_words
               #for i in range(min(len(highlights_num),len(highlights_words))):
               for i in range(len(highlights_num)):
                   item=ShinnnItem()
                   item['link']=r"http://bbs.hupu.com/"+list[0]+".html"
                   item['title']=list[1]

                   try:
                        item['content']=highlights_words[i]
                   except IndexError:
                        item['content']='There is a bug!!!'


                   item['number']=highlights_num[i]

                   items.append(item)


           else:continue

           f.write(link+'\n\n\n\n')
       return items

       f.close()



