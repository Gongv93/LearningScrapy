# Scrapy settings for example_2 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'swift'

SPIDER_MODULES = ['example_2.spiders']
NEWSPIDER_MODULE = 'example_2.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'example_2 (+http://www.yourdomain.com)'

FEED_URI = "scraped_data.json"
FEED_FORMAT = "json"

ITEM_PIPELINES = {
    'example_2.pipelines.SwiftPipeline': 300
}