# -*- coding: utf-8 -*-
import scrapy

from ..items import AlpinabookItem

class AlphSpider(scrapy.Spider):
    name = 'alph'
    start_urls = [
        'https://www.alpinabook.ru/catalog/books-lichnaya-effektivnost/',
        'https://www.alpinabook.ru/catalog/books-self-confidence/',
        'https://www.alpinabook.ru/catalog/books-time-managment/',
        'https://www.alpinabook.ru/catalog/books-leadership/',
        'https://www.alpinabook.ru/catalog/books-emotional-intelligence/',
        'https://www.alpinabook.ru/catalog/books-brain-development/',
        'https://www.alpinabook.ru/catalog/books-critical-thinking/',
        'https://www.alpinabook.ru/catalog/books-hobby-traveling-cars/',
        'https://www.alpinabook.ru/catalog/books-motivation/',
        'https://www.alpinabook.ru/catalog/books-popular-science/',
        'https://www.alpinabook.ru/catalog/books-psihologiya/',
        'https://www.alpinabook.ru/catalog/books-business/',
        'https://www.alpinabook.ru/catalog/books-business/',
        'https://www.alpinabook.ru/catalog/books-for-parents-and-children/',
        'https://www.alpinabook.ru/catalog/books-marketing-advertising-pr/',
        'https://www.alpinabook.ru/catalog/books-economics-politics-sociology/',
        'https://www.alpinabook.ru/catalog/books-health-yoga-beauty/',
        'https://www.alpinabook.ru/catalog/books-art-and-creativity/',
        'https://www.alpinabook.ru/catalog/books-ezhednevniki-i-bloknoty/',
        'https://www.alpinabook.ru/catalog/books-gifts-and-sets/',
        'https://www.alpinabook.ru/catalog/books-gifts-and-sets/',
        'https://www.alpinabook.ru/catalog/books-biblioteka-sberbanka/'
    ]

    def parse(self, response):
        book_url = 'https://www.alpinabook.ru'
        rub = ' ₽'
        for alph in response.css('.categoryBooks'):
            yield{
                'Url': book_url + alph.css('a.ddl_product_link::attr(href)').get(),
                'Name': alph.css('p.nameBook::text').get(),
                'Author': alph.css('p.bookAutor::text').get(),
                'Price': alph.css('p.priceOfBook span::text').get() + rub,
                'img_book': book_url + alph.css('div.section_item_img img::attr(src)').get()
            }

        # пагинация
        next_page = response.css('li.bx-pag-next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    # scrapy crawl alph