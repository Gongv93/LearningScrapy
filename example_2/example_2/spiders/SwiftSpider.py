from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http.request import Request

from example_2.items import Articles

class SwiftSpider( CrawlSpider ) :
	name =   "swift";
	allowed_domains = [ "swift.mkrsqr.com" ];
	start_urls = [ "http://swift.mkrsqr.com/" ];
	rules  = ( Rule( 
					SgmlLinkExtractor( allow = ('/blog/\d+/\d+/\d+/.*',), unique =  True ), 
					callback = 'parse_news' 
			),		
	);		

	def parse_news( self, response ) :
		sel = Selector(response);

		item = Articles();
		item[ 'url' ] = response.url;
		item[ 'title' ] = sel.xpath( "//article/header/h1/text()" ).extract();

		return item;