# Scrapy settings for example_3 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'RSc'

SPIDER_MODULES = ['example_3.spiders']
NEWSPIDER_MODULE = 'example_3.spiders'

FEED_URI = "scraped_data.json"
FEED_FORMAT = "json"