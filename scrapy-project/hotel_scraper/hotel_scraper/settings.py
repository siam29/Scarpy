BOT_NAME = "hotel_scraper"
SPIDER_MODULES = ["hotel_scraper.spiders"]
NEWSPIDER_MODULE = "hotel_scraper.spiders"
ROBOTSTXT_OBEY = True
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

FEED_FORMAT = 'json'
FEED_URI = 'scrapy_output/hotels_combined_data.json'

DOWNLOAD_DELAY = 2
