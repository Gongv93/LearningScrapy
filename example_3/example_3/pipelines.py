# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class Example3Pipeline(object):
    def process_item(self, item, spider):
    	if not item[ 'comment' ] :
    		item[ 'comment' ] = "Comment N/A";
    		
        return item
