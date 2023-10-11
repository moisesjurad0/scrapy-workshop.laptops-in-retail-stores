import scrapy

from scrapy_laptops_in_retail_stores.items import Laptop2


class LaptopsripleySpider(scrapy.Spider):
    name = "ripley"
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    # allowed_domains = ["simple.ripley.com.pe"]
    start_urls = [
        # "https://simple.ripley.com.pe/tecnologia/computacion-gamer/laptops-gamer",
        # "https://simple.ripley.com.pe/tecnologia/computacion-gamer/laptops-gamer?source=menu&s=mdco",
        "https://simple.ripley.com.pe/tecnologia/computacion-gamer/laptops-gamer?source=menu&page=1",
        "https://simple.ripley.com.pe/tecnologia/computacion/laptops?source=menu&page=1"
    ]

    def parse(self, response):
        for i in response.css("div.catalog-product-details"):
            item = Laptop2(
                origin="ripley",
                name=i.css("div.catalog-product-details__name::text").get(),
                price_offered=i.css("li.catalog-prices__offer-price::text").get(),
                price_with_card=i.css("li.catalog-prices__card-price::text").get(),
                price_regular=i.css("li.catalog-prices__list-price::text").get())
            yield item

        # CALLING NEXT PAGE
        yield from response.follow_all(css="ul.pagination > li > a", callback=self.parse)
