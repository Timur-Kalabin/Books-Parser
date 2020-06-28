# -*- coding: utf-8 -*-
import scrapy

from ..items import KnigaItem

class KnigaParseSpider(scrapy.Spider):
    name = 'kniga_parse'

    start_urls = [
        'https://inet-kniga.ru/catalog/744/',
        'https://inet-kniga.ru/catalog/742/',
        'https://inet-kniga.ru/catalog/746/',
        'https://inet-kniga.ru/catalog/1099/',
        'https://inet-kniga.ru/catalog/749/',
        'https://inet-kniga.ru/catalog/750/',
        'https://inet-kniga.ru/catalog/751/',
        'https://inet-kniga.ru/catalog/752/',
        'https://inet-kniga.ru/catalog/979/',
        'https://inet-kniga.ru/catalog/1326/',
        'https://inet-kniga.ru/catalog/1551/',
        'https://inet-kniga.ru/catalog/912/',
        'https://inet-kniga.ru/catalog/1310/',
        'https://inet-kniga.ru/catalog/961/',
        'https://inet-kniga.ru/catalog/1094/',
        'https://inet-kniga.ru/catalog/1095/',
        'https://inet-kniga.ru/catalog/1098/',
        'https://inet-kniga.ru/catalog/1279/',
        'https://inet-kniga.ru/catalog/966/',
        'https://inet-kniga.ru/catalog/733/',
        'https://inet-kniga.ru/catalog/895/',
        'https://inet-kniga.ru/catalog/861/',
        'https://inet-kniga.ru/catalog/706/',
        'https://inet-kniga.ru/catalog/907/',
        'https://inet-kniga.ru/catalog/1029/',
        'https://inet-kniga.ru/catalog/753/',
        'https://inet-kniga.ru/catalog/782/',
        'https://inet-kniga.ru/catalog/1093/',
        'https://inet-kniga.ru/catalog/855/',
        'https://inet-kniga.ru/catalog/808/',
        'https://inet-kniga.ru/catalog/825/',
        'https://inet-kniga.ru/catalog/838/',
        'https://inet-kniga.ru/catalog/980/',
        'https://inet-kniga.ru/catalog/877/',
        'https://inet-kniga.ru/catalog/916/',
        'https://inet-kniga.ru/catalog/768/',
        'https://inet-kniga.ru/catalog/848/'
    ]

    def parse(self, response):
        kniga_url = 'https://inet-kniga.ru'
        for kniga_parse in response.css('.custom_showcase1'):
            yield{
                'Url': kniga_url + kniga_parse.css('a.catalog-section-link::attr(href)').get(),
                'Name': kniga_parse.css('p.namecatalog::text').get(),
                'Author': kniga_parse.css('p.avtorcatalog::text').get(),
                'Price': kniga_parse.css('span.money::text').get(),
                'img_book': kniga_url + kniga_parse.css('img.normal-img::attr(src)').get()
            }
            
    # scrapy crawl kniga_parse