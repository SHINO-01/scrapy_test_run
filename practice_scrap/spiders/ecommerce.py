import scrapy
from practice_scrap.items import PracticeScrapItem

class EcommerceSpider(scrapy.Spider):
    name = 'ecommerce'
    start_urls = ['https://www.scrapingcourse.com/ecommerce/']

    def parse(self, response):
        self.logger.info(f"Processing URL: {response.url}")
        for product in response.css('a.woocommerce-LoopProduct-link'):
            item = PracticeScrapItem()
            item['title'] = product.css('h2.woocommerce-loop-product__title::text').get()
            item['price'] = product.css('span.woocommerce-Price-amount bdi::text').get()
            item['image_urls'] = [product.css('img.attachment-woocommerce_thumbnail::attr(src)').get()]
            item['product_url'] = product.css('::attr(href)').get()
            
            # Log extracted item for debugging
            self.logger.info(f"Extracted Item: {item}")
            yield item
