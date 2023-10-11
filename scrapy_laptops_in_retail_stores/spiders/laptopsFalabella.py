import scrapy
from scrapy_laptops_in_retail_stores.items import Laptop2
import pprint as pp


class LaptopsfalabellaSpider(scrapy.Spider):
    name = "falabella"
    allowed_domains = ["falabella.com.pe"]
    start_urls = [
        "https://www.falabella.com.pe/falabella-pe/category/cat40712/Laptops?page=1",
        "https://www.falabella.com.pe/falabella-pe/collection/notebook-gamer?page=1",
    ]

    def parse(self, response):
        for i in response.xpath('//*[@id="testId-searchResults-products"]/div'):            
            item = Laptop2(
                origin="falabella",
                name=i.xpath("a/div[1]/div[1]/section/picture/img/@alt").get(),
                price_offered=i.css("li[data-internet-price]::attr(data-internet-price)").get(),
                price_with_card=i.css("li[data-cmr-price]::attr(data-cmr-price)").get(),
                price_regular=i.css("li[data-normal-price]::attr(data-normal-price)").get())           
            yield item

        # USE THIS when the NEXT button has a URL attrib of someking
        # yield from response.follow_all(css="ul.pagination > li > a", callback=self.parse)

        next_page_url = self.get_next_page_url(response)
        
        # CALL THIS method to run among all the pages 1,2,3,4,5..156,157,158..
        # if next_page_url:
        #     yield response.follow(next_page_url, callback=self.parse)
        
        # ***the data loaded in these pages is the same***
        # recomended solution 1: use scrapy splash or another scraper bases on browser (scrapy by default uses requests)
        # recomended solution 2: locate APIs to get direct data.
        
        # if that don't work You need to reverse engineer how..
        # your page generated this url (from the first image):

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
    
        # try using the API
        # https://medium.com/@geneng/web-crawling-made-easy-with-scrapy-and-rest-api-ed993e84abd3
        # https://github.com/canyousayyes/scrapy-web-crawler-by-rest-api
