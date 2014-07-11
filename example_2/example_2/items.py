# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class Articles(Item):
	title  = Field();
	catag  = Field();
	author = Field();
	date   = Field();
	source = Field();
	link   = Field();