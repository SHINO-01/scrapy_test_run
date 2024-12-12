import scrapy
from practice_scrap.items import PracticeScrapItem

class EcommerceSpider(scrapy.Spider):
    name = 'ecommerce'
    start_urls = ['https://www.scrapingcourse.com/ecommerce/']

    def parse(self, response):
        # Log the current URL being processed
        self.logger.info(f"Processing URL: {response.url}")
        
        # Loop through each product block
        for product in response.css('a.woocommerce-LoopProduct-link'):
            item = PracticeScrapItem()
            
            # Extract product details
            item['title'] = product.css('h2.product-name::text').get()
            item['price'] = product.css('span.woocommerce-Price-amount bdi::text').get()
            item['image_url'] = product.css('img::attr(src)').get()
            item['product_url'] = product.css('::attr(href)').get()

            # Log extracted details for debugging
            self.logger.info(f"Extracted Item: {item}")
            
            yield item