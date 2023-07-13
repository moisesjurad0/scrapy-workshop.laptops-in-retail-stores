# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from dataclasses import dataclass
import attr


class ScrapyLaptopsInRetailStoresItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Laptop(scrapy.Item):
    origin = scrapy.Field()
    name = scrapy.Field()
    price_offered = scrapy.Field()
    price_with_card = scrapy.Field()
    price_regular = scrapy.Field()


@dataclass
class Laptop2:
    origin: str
    name: str
    price_offered: str
    price_with_card: str
    price_regular: str


@attr.s
class Laptop3:
    origin = attr.ib()
    name = attr.ib()
    price_offered = attr.ib()
    price_with_card = attr.ib()
    price_regular = attr.ib()
