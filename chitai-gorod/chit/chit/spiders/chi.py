# -*- coding: utf-8 -*-
import scrapy

from ..items import ChitItem


class ChiSpider(scrapy.Spider):
    name = 'chi'
    start_urls = [
        'https://m.chitai-gorod.ru/catalog/books/khudozhestvennaya_literatura-9657/?page=1',
        'https://m.chitai-gorod.ru/catalog/books/knigi_dlya_detey-9072/?page=1',
        'https://m.chitai-gorod.ru/catalog/books/obrazovaniye-9405/?page=1',
        'https://m.chitai-gorod.ru/catalog/books/nauka_i_tekhnika-9170/?page=1',
        'https://m.chitai-gorod.ru/catalog/books/obshchestvo-9304/?page=1',
        'https://m.chitai-gorod.ru/catalog/books/delovaya_literatura-8979/?page=1',
        'https://m.chitai-gorod.ru/catalog/books/krasota_zdorovye_sport-9116/?page=1',
        'https://m.chitai-gorod.ru/catalog/books/uvlecheniya-9564/?page=1',
        'https://m.chitai-gorod.ru/catalog/books/psikhologiya-9530/?page=1',
        'https://m.chitai-gorod.ru/catalog/books/ezoterika-9705/?page=1',
        'https://m.chitai-gorod.ru/catalog/books/filosofiya_i_religiya-9645/?page=1',
        'https://m.chitai-gorod.ru/catalog/books/iskusstvo-9035/?page=1',
        'https://m.chitai-gorod.ru/catalog/books/podarochnyye_izdaniya-9469/?page=1',
        'https://m.chitai-gorod.ru/catalog/books/knigi_na_inostrannykh_yazykakh-9154/?page=1'
    ]

    def parse(self, response):
        chitai_gorod = 'https://www.chitai-gorod.ru'

        for chi in response.css('.medium-6'):
            yield{
                'Url': chitai_gorod + chi.css('a.js-analytic-productlink::attr(href)').get(),
                'Name': chi.css('div.big-card-title::text').get(),
                'Author': chi.css('div.big-card-author::text').get(),
                'Price': chi.css('div.big-card-price b::text').get(),
                'img_book': chi.css('img::attr(data-src)').get()
            }


        # items = ChitItem()

        # Url = chitai_gorod + response.css('.js-analytic-productlink::attr(href)').get()
        # Name = response.css('.big-card-title::text').getall()
        # Author = response.css('.big-card-author::text').getall()
        # Price = response.css('.big-card-price b::text').getall()
        # img_book = response.css('.lazyloaded::attr(src)').getall()

        # items['Url'] = Url
        # items['Name'] = Name
        # items['Author'] = Author
        # items['Price'] = Price
        # items['img_book'] = img_book

        # yield items

        # пагинация
        next_page = response.css('li.pagination-next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
            

    # scrapy crawl chi