import scrapy


class LaptopsoechsleSpider(scrapy.Spider):
    name = "laptopsOechsle"
    allowed_domains = ["www.oechsle.pe"]
    start_urls = ["https://www.oechsle.pe/tecnologia/computo/laptops"]

    def parse(self, response):

        # for quote in response.css("div.product.instock.hideTagPrice"):
        for quote in response.css("div.product.instock"):
            yield {
                "nombre": quote.attrib['data-name'],
                # "nombre2": quote.css("div.productImage.prod-img.img_one img").attrib['alt'],
                # "precio": quote.attrib['data-product-price'],
                # "precio_sin_dcto": quote.attrib['data-product-list-price']
                "precio1": quote.css("span.BestPrice::text").get(),
                "precio2": quote.css("span.ListPrice::text").get(),
            }

        yield from response.follow_all(css="a.page-link", callback=self.parse)
