import scrapy
from urllib.parse import urljoin


class LaptopsoechsleSpider(scrapy.Spider):
    name = "laptopsOechsle"
    allowed_domains = ["www.oechsle.pe"]
    start_urls = [
        "https://www.oechsle.pe/tecnologia/computo/laptops?page=1",
        "https://www.oechsle.pe/tecnologia/computo/laptops-gamers?page=1",
    ]

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

        # yield from response.follow_all(css="a.page-link",
        # callback=self.parse)

        # Get the URL for the next page
        next_page_url = self.get_next_page_url(response)

        if next_page_url:
            yield response.follow(next_page_url, callback=self.parse)

    def get_next_page_url(self, response):
        # string1='?&optionOrderBy=OrderByScoreDESC&O=OrderByScoreDESC&page='

        # Logic to determine the URL for the next page
        current_url = response.url
        current_page_number = int(current_url.split('=')[-1])
        current_url_without_page = current_url.split(
            '=')[0]  # Remove "page1" from the URL

        next_page_number = current_page_number + 1
        # next_page_url = urljoin(current_url, f'{string1}{next_page_number}')
        next_page_url = urljoin(
            current_url_without_page,
            f'={next_page_number}')

        return next_page_url
