import scrapy
from urllib.parse import urljoin
import pprint as pp


class LaptopsoechsleSpider(scrapy.Spider):
    name = "laptopsOechsle"
    allowed_domains = ["www.oechsle.pe"]
    start_urls = [
        "https://www.oechsle.pe/tecnologia/computo/laptops-gamers?page=1",
        # "https://www.oechsle.pe/tecnologia/computo/laptops-gamers?page=2",
        # "https://www.oechsle.pe/tecnologia/computo/laptops-gamers?page=3",
        # "https://www.oechsle.pe/tecnologia/computo/laptops?page=1",
        # "https://www.oechsle.pe/tecnologia/computo/laptops?&optionOrderBy=OrderByScoreDESC&O=OrderByScoreDESC&page=1",
    ]

    def parse(self, response):
        for quote in response.css("div.product.instock"):  # .hideTagPrice
            yield {
                "name": quote.attrib['data-name'],
                # "nombre2": quote.css("div.productImage.prod-img.img_one img").attrib['alt'],
                # "precio": quote.attrib['data-product-price'],
                # "precio_sin_dcto": quote.attrib['data-product-list-price']
                "price-online": quote.css("span.BestPrice::text").get(),
                "price-with-Card": None,
                "price-regular": quote.css("span.ListPrice::text").get(),
            }

        # yield from response.follow_all(css="a.page-link",
        # callback=self.parse)

        # next_page_url = self.get_next_page_url(response)
        # if next_page_url:
        #     yield response.follow(next_page_url, callback=self.parse)

    def get_next_page_url(self, response):
        current_url = response.url
        current_page_number = int(current_url.split('=')[-1])
        current_url_without_page = f"{current_url.rsplit('=',1)[0]}="
        next_page_number = current_page_number + 1
        # next_page_url = urljoin(current_url, f'{string1}{next_page_number}')
        next_page_url = f'{current_url_without_page}{next_page_number}'

        print('-----------------------------------------------------------')
        print('')
        print('')
        print('')
        print('PRINT-BEGIN')
        pp.pprint(f"current_url=>{current_url}")
        pp.pprint(f"current_page_number=>{current_page_number}")
        pp.pprint(f"current_url_without_page=>{current_url_without_page}")
        pp.pprint(f"next_page_number=>{next_page_number}")
        pp.pprint(f"next_page_url=>{next_page_url}")
        print('PRINT-END')
        print('')
        print('')
        print('')
        print('-----------------------------------------------------------')

        return next_page_url
