from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http.request import Request

from example_2.items import Articles

class SwiftSpider( CrawlSpider ) :
	name =   "swift";
	allowed_domains = [ "swift.mkrsqr.com" ];
	start_urls = [ "http://swift.mkrsqr.com/page/1" ];
	rules  = ( Rule( 
					SgmlLinkExtractor( allow = ('/page/.*', '/blog/\d+/\d+/\d+/.*', ), unique =  True ), 
					callback = 'parse_news',
					follow = True
			),		
	);		

	def parse_news( self, response ) :
		sel = Selector(response);
		
		item = Articles();
		if 'blog' in response.url :
			item[ 'title' ] = sel.xpath( '//article/header/h1/text()' ).extract();
			item[ 'catag' ] = sel.xpath( '//span[@class="cat-links"]/a/text()' ).extract();
			item[ 'author' ] = sel.xpath( '//span[@class="byline author vcard"]/a/text()' ).extract();
			item[ 'date' ] = sel.xpath( '//span[@class="entry-date"]/a/time/text()' ).extract();
			item[ 'source' ] = sel.xpath( '//div[@class="entry-content"]/p[last()]/text()' ).extract();
		
		return item;