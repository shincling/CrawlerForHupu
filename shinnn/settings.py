# Scrapy settings for shinnn project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'Mozaration 0.9.325'
BOT_VERSION = '1.6'

SPIDER_MODULES = ['shinnn.spiders']
NEWSPIDER_MODULE = 'shinnn.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES=['shinnn.pipelines.ShinnnPipeline']