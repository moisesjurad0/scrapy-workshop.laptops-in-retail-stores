import scrapy
from urllib.parse import urljoin
from scrapy_splash import SplashRequest
import pprint as pp


class LaptopsoechsleSpider(scrapy.Spider):
    name = "laptopsOechsle"
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'

    def start_requests(self):
        urls = [
            # "https://www.oechsle.pe/tecnologia/computo/laptops?page=1",
            "https://www.oechsle.pe/tecnologia/computo/laptops-gamers?page=1",
            # "https://www.oechsle.pe/tecnologia/computo/laptops-gamers?page=2",
            # "https://www.oechsle.pe/tecnologia/computo/laptops-gamers?page=3",
            # "https://www.oechsle.pe/tecnologia/computo/laptops-gamers?page=4",
            # "https://www.oechsle.pe/tecnologia/computo/laptops-gamers?page=5",
        ]

        urls_pintar = []
        for url in urls:
            urls_pintar.append(
                SplashRequest(url, callback=self.parse, args={'wait': 5}))
        print('-----------------------------------------------------------')
        print('')
        print('')
        print('')
        print('urls_pintar-BEGIN')
        pp.pprint(urls_pintar)
        print('urls_pintar-END')
        print('')
        print('')
        print('')
        print('-----------------------------------------------------------')
        return urls_pintar

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
        print('-----------------------------------------------------------')
        print('')
        print('')
        print('')
        print('urls_to_follow-BEGIN')
        pp.pprint(urls_to_follow)
        print('urls_to_follow-END')
        print('')
        print('')
        print('')
        print('-----------------------------------------------------------')
        for url in urls_to_follow:
            yield SplashRequest(url, self.parse, args={'wait': 5})
