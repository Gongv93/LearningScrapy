from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector,HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor


from example_3.items import RedditItems

class Rsc_Spider(CrawlSpider) :
	name = 'RSc';
	allowed_domain = [ 'www.reddit.com' ];
	start_urls = [ 'http://www.reddit.com/r/starcraft/' ];
	rules = (
			# Only in Sc subreddit
			Rule( SgmlLinkExtractor(allow  = 'reddit.com/r/starcraft/\w+',
									unique = True),
				  callback = 'parse_item',
				  follow    = True),
		)

	def parse_item(self, response) :
		sel = Selector(response);
		item = RedditItems();
		# If page is a comment
		if 'comment' in response.url and not 'related' in response.url :
			item[ 'comment' ] = sel.xpath('//div[@class="sitetable nestedlisting"]/div[1]/div[2]//div[@class="md"]/p/text()').extract();
			item[ 'title' ] = sel.xpath('//p[@class="title"]/a/text()').extract();

		return item
