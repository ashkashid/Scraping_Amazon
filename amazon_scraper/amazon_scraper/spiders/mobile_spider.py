import scrapy
from ..items import MobileItem

class MobileSpider(scrapy.Spider):
    name = 'mobile_spider'
    allowed_domains = ['amazon.in']
    start_urls = ['https://www.amazon.in/s?k=mobile+phone']

    def parse(self, response):
        for product in response.css('.s-result-item'):
            item = MobileItem()
            item['name'] = product.css('.a-size-medium::text').get()
            item['processor'] = product.css('.a-row .a-color-secondary:nth-child(2)::text').get()
            item['ram'] = product.css('.a-row .a-color-secondary:nth-child(3)::text').get()
            item['storage'] = product.css('.a-row .a-color-secondary:nth-child(4)::text').get()
            item['display'] = product.css('.a-row .a-color-secondary:nth-child(5)::text').get()
            item['camera'] = product.css('.a-row .a-color-secondary:nth-child(6)::text').get()
            item['battery'] = product.css('.a-row .a-color-secondary:nth-child(7)::text').get()
            yield item


        # Follow the next page link if available
        next_page = response.css('.s-pagination-item.s-pagination-next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
