import scrapy

from scrapy.loader import ItemLoader

from ..items import UnitybankngItem
from itemloaders.processors import TakeFirst


class UnitybankngSpider(scrapy.Spider):
	name = 'unitybankng'
	start_urls = ['https://www.unitybankng.com/media/pressrelease']

	def parse(self, response):
		post_links = response.xpath('//h4/a/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

	def parse_post(self, response):
		title = response.xpath('//h4/a/text()').get()
		description = response.xpath('//div[@class="main_content text-justify"]//text()[normalize-space()]').getall()
		description = [p.strip() for p in description if '{' not in p]
		description = ' '.join(description).strip()
		date = response.xpath('//span[@class="date"]/text()').get()

		item = ItemLoader(item=UnitybankngItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
