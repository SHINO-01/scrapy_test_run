import scrapy

class PracticeScrapItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    image_urls = scrapy.Field()  # Required by ImagesPipeline
    images = scrapy.Field()  # Stores download results
    product_url = scrapy.Field()
    image_path = scrapy.Field()  # Populated by CustomImagesPipeline
