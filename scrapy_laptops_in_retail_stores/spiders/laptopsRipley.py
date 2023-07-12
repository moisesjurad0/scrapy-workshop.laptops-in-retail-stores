import scrapy


class LaptopsripleySpider(scrapy.Spider):
    name = "laptopsRipley"
    allowed_domains = ["simple.ripley.com.pe"]
    start_urls = ["https://simple.ripley.com.pe/tecnologia/computacion-gamer/laptops-gamer"]

    def parse(self, response):
        for quote in response.css("div.catalog-product-details"):  # .hideTagPrice
            yield {
                "name": quote.css("div.catalog-product-details__name::text").get(),
                "price-online": quote.css("li.catalog-prices__offer-price::text").get(),
                "price-with-Card": quote.css("li.catalog-prices__card-price::text").get(),
                "price-regular": quote.css("li.catalog-prices__list-price::text").get(),
            }

        # yield from response.follow_all(css="a.page-link",
        # callback=self.parse)

