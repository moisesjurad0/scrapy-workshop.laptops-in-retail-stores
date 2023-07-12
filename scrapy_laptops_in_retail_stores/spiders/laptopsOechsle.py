import scrapy
from urllib.parse import urljoin
from scrapy_splash import SplashRequest
import pprint as pp

class LaptopsoechsleSpider(scrapy.Spider):
    name = "laptopsOechsle"

    def start_requests(self):
        urls = [
            # "https://www.oechsle.pe/tecnologia/computo/laptops?page=1",
            "https://www.oechsle.pe/tecnologia/computo/laptops-gamers?page=1",
            "https://www.oechsle.pe/tecnologia/computo/laptops-gamers?page=2",
            "https://www.oechsle.pe/tecnologia/computo/laptops-gamers?page=3",
            "https://www.oechsle.pe/tecnologia/computo/laptops-gamers?page=4",
            "https://www.oechsle.pe/tecnologia/computo/laptops-gamers?page=5",
        ]
        retorno = []
        for url in urls:
            retorno.append(
                SplashRequest(url, callback=self.parse, args={'wait': 5})
            )
        pp.pprint(retorno)
        return retorno

    def parse(self, response):

        for quote in response.css("div.product.instock"):
            yield {
                "nombre": quote.attrib['data-name'],
                # "nombre2": quote.css("div.productImage.prod-img.img_one img").attrib['alt'],
                # "precio": quote.attrib['data-product-price'],
                # "precio_sin_dcto": quote.attrib['data-product-list-price']
                "precio1": quote.css("span.BestPrice::text").get(),
                "precio2": quote.css("span.ListPrice::text").get(),
            }

        # yield from response.follow_all(css="a.page-link",
        # callback=self.parse)
        urls_to_follow = response.css('a.page-link').getall()
        for url in urls_to_follow:
            yield SplashRequest(url, self.parse, args={'wait': 5})
