import scrapy


class LaptopsoechsleSpider(scrapy.Spider):
    name = "laptopsOechsle"
    allowed_domains = ["www.oechsle.pe"]
    start_urls = ["https://www.oechsle.pe/tecnologia/computo/laptops"]

    def parse(self, response):
        pass
