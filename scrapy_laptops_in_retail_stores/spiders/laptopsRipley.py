import scrapy


class LaptopsripleySpider(scrapy.Spider):
    name = "laptopsRipley"
    allowed_domains = ["simple.ripley.com.pe"]
    start_urls = ["https://simple.ripley.com.pe/tecnologia/computacion/laptops?source=menu"]

    def parse(self, response):
        pass
