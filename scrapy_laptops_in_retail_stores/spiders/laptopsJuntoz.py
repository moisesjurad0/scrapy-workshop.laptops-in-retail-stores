import scrapy


class LaptopsjuntozSpider(scrapy.Spider):
    name = "laptopsJuntoz"
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
            yield {
                "origin": "juntoz",
                "name": i.css("div.product-preview-card__wrapper__footer__product-name > a::text").get(),
                "price-offered": i.css("span[jztm-prop='price']::text").get(),
                "price-with-Card": None,
                "price-regular": i.css("span[jztm-prop='specialPrice']::text").get(),
            }

        # yield from response.follow_all(css="ul.pagination > li > a",
        # callback=self.parse)
