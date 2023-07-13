import scrapy


class LaptopsfalabellaSpider(scrapy.Spider):
    name = "laptopsFalabella"
    allowed_domains = ["falabella.com.pe"]
    start_urls = [
        "https://www.falabella.com.pe/falabella-pe/category/cat40712/Laptops",
        "https://www.falabella.com.pe/falabella-pe/collection/notebook-gamer",
    ]

    def parse(self, response):
        for quote in response.css("div.catalog-product-details"):
            yield {
                "origin": "falabella",
                "type": "gamer" if response.url.contains("gamer") else "regular",
                "name": quote.css("div.catalog-product-details__name::text").get(),
                "price-offered": quote.css("li.catalog-prices__offer-price::text").get(),
                "price-with-Card": quote.css("li.catalog-prices__card-price::text").get(),
                "price-regular": quote.css("li.catalog-prices__list-price::text").get(),
            }

        yield from response.follow_all(css="ul.pagination > li > a", callback=self.parse)
