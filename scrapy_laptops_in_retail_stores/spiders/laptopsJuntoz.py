import scrapy

from scrapy_laptops_in_retail_stores.items import Laptop, Laptop2


class LaptopsjuntozSpider(scrapy.Spider):
    name = "juntoz"
    allowed_domains = ["juntoz.com"]
    start_urls = [
        # "https://juntoz.com/categorias/tecnologia/computacion/laptops", # normal
        # "https://juntoz.com/categorias/tecnologia/gaming/laptops-gamer", # gamer
        "https://juntoz.com/catalogo?categoryId=995891&top=100&skip=0&orderBy=rating-desc",  # gamer
        "https://juntoz.com/catalogo?categoryId=995878&top=2000&skip=0&orderBy=rating-desc",  # normal
    ]
    # user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'

    def parse(self, response):
        for i in response.css("div.product-preview-card__wrapper__footer"):
            item = Laptop2(
                origin="juntoz",
                name=i.css("div.product-preview-card__wrapper__footer__product-name > a::text").get(),
                price_offered=i.css("span[jztm-prop='price']::text").get(),
                price_with_card=None,
                price_regular=i.css("span[jztm-prop='specialPrice']::text").get())
            yield item

        # yield from response.follow_all(css="ul.pagination > li > a",
        # callback=self.parse)
