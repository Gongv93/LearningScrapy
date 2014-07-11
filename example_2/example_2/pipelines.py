# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re

class SwiftPipeline(object):
    def process_item(self, item, spider):
    	
    	if item :
    		# Splits source into the article source and the link
	    	if item[ 'source' ] :
	    		tempSource = item[ 'source' ][0]
	    		urlStart = tempSource.find("http://");
	    		if urlStart == -1 :
	    			item[ 'link' ] = 'N/A';
	    		else :
		    		item[ 'link' ] = tempSource[urlStart:];
		    		item[ 'source' ] = tempSource[4:urlStart-1];
		    		
        return item
