# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItebooksScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()             # 书名。
    author = scrapy.Field()
    isbn = scrapy.Field()
    year = scrapy.Field()
    pages = scrapy.Field()
    language = scrapy.Field()
    file_size = scrapy.Field()
    category = scrapy.Field()

    thumbnail = scrapy.Field()          # 书封面的缩略图。
    # book_description = scrapy.Field()   # 内容简介
    pdf_download_url = scrapy.Field()

