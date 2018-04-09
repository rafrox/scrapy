from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem


class Advent(BasePortiaSpider):
    name = "advent"
    allowed_domains = [u'www.adventgames.com.au']
    start_urls = [u'http://www.adventgames.com.au/c/4504822/1/all-games-a---k.html',
                  {u'url': u'http://www.adventgames.com.au/Listing/Category/?categoryId=4504822&page=[1-5]',
                   u'fragments': [{u'valid': True,
                                   u'type': u'fixed',
                                   u'value': u'http://www.adventgames.com.au/Listing/Category/?categoryId=4504822&page='},
                                  {u'valid': True,
                                   u'type': u'range',
                                   u'value': u'1-5'}],
                   u'type': u'generated'}]
    rules = [
        Rule(
            LinkExtractor(
                allow=('.*'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [
        [
            Item(
                PortiaItem,
                None,
                u'.DataViewCell > form > table',
                [
                    Field(
                        u'Title',
                        'tr:nth-child(1) > td > .DataViewItemProductTitle > a *::text',
                        []),
                    Field(
                        u'Price',
                        'tr:nth-child(1) > td > .DataViewItemOurPrice *::text',
                        []),
                    Field(
                        u'Img_src',
                        'tr:nth-child(1) > td > .DataViewItemThumbnailImage > div > a > img::attr(src)',
                        []),
                    Field(
                        u'URL',
                        'tr:nth-child(1) > td > .DataViewItemProductTitle > a::attr(href)',
                        []),
                    Field(
                        u'Stock',
                        'tr:nth-child(2) > td > .DataViewItemAddToCart > .wButton::attr(value)',
                        [])])]]
