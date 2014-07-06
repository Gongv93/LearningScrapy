from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from example_2.items import Articles

class SwiftSpider( CrawlSpider ) :
	name =   "swift";
	allowed_domains = [ "swift.mkrsqr.com" ];
	start_urls = [ "http://swift.mkrsqr.com/" ];
	rules  = ( Rule( 
					SgmlLinkExtractor( allow = ('/?p=\d+',), unique =  True ), 
					callback = 'parse_news' 
			),		
	);		

	def parse_news( self, response ) :
		item = Articles();
		item[ 'url' ] = response.url;
		#item[ 'title' ]    = response.xpath( '//article/header/h1/text()' ).extract();
		#tem[ 'desc' ]   = response.xpath( '//article/div/table/tbody/tr/td[2]/font/div[2]/font[2]/text()' ).extract();
		return item;