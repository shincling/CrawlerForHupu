# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

class ShinnnPipeline(object):
    def __init__(self):
        self.file=open(r'e:\test\hupu.txt','wb')
    def process_item(self, item, spider):
        self.file.write(item['title'] + '\t'+ item['link'] + '\t' + item['content']+item['number']+'\n')
        return item
