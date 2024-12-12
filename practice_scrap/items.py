import scrapy

class PracticeScrapItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    image_url = scrapy.Field()
    product_url = scrapy.Field()
    images = scrapy.Field()  # Added to store image download results from ImagesPipeline
    image_path = scrapy.Field()  # To store the path of downloaded images
