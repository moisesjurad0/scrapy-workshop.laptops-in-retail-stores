import scrapy


class LaptopsoechsleSpider(scrapy.Spider):
    name = "laptopsOechsle"
    allowed_domains = ["www.oechsle.pe"]
    start_urls = ["https://www.oechsle.pe/tecnologia/computo/laptops"]

    def parse(self, response):

        # for quote in response.css("div.product.instock.hideTagPrice"):
        for quote in response.css("div.product.instock"):
            yield {
                "nombre": quote.attrib['data-name'].get(),
                "precio": quote.attrib['data-product-price'].get(),
                "precio_sin_dcto": quote.attrib['data-product-list-price'].get()
            }

        yield from response.follow_all(css="a.page-link", callback=self.parse)
