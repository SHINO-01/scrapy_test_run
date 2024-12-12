# Scrapy settings for practice_scrap project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'practice_scrap'

SPIDER_MODULES = ['practice_scrap.spiders']
NEWSPIDER_MODULE = 'practice_scrap.spiders'

ROBOTSTXT_OBEY = False

USER_AGENT = 'scraping_course (+https://www.scrapingcourse.com/ecommerce/)'

DOWNLOAD_DELAY = 2

FEED_EXPORT_ENCODING = 'utf-8'

ITEM_PIPELINES = {
    'practice_scrap.pipelines.CustomImagesPipeline': 1,
    'practice_scrap.pipelines.PracticeScrapPipeline': 300,
}

IMAGES_STORE = 'media/images'  # Folder for images
MEDIA_ALLOW_REDIRECTS = True  # Handle redirects if necessary


AUTOTHROTTLE_ENABLED = True

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

DATABASE = {
    'drivername': 'postgresql',
    'host': 'postgres',  # Docker service name for PostgreSQL
    'port': '5432',
    'username': 'scrapy_user',
    'password': 'scrapy_pass',
    'database': 'scrapyDB',
}
