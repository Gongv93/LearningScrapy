from scrapy.spider import Spider
from scrapy.selector import Selector

from example_2.items import Articles

class SwiftSpider( Spider ) :
	name 			=   "swift";
	allowed_domains = [ "http://swift.mkrsqr.com/" ]
	start_urls 		= [ "http://swift.mkrsqr.com/" ]

	def parse( self, response ) :
		sel   = Selector(response);
		sites = sel.xpath( '//article' );
		items = []

		for site in sites :
			item = Articles();
			item[ 'title' ]  = site.xpath( 'div[@class="entry-inner"]/header/h2[@class="entry-title"]/text()' ).extract();
			item[ 'desc' ]   = site.xpath( 'div[@class="entry-inner"]/div[@class="entry-content"]/p/a/text()' ).extract();
			items.append(item);
		return items;