# -*- coding: utf-8 -*-
import scrapy,re
from itEbooks_Scrapy.items import ItebooksScrapyItem

class EbookspiderSpider(scrapy.Spider):
    name = 'eBookSpider'
    allowed_domains = ['allitebooks.org']
    start_urls = ['http://www.allitebooks.org/']

    def parse(self, response):                      # 解析网站主页列表。
        articles = response.xpath('//*[@id="main-content"]/div/article')
        for article in articles:
            detail_page_url = article.xpath('./div[1]/a/@href').extract_first()
            yield scrapy.Request(url=detail_page_url,callback=self.detail_parse)    # 获得的书的详情页再次发送请求

        total_page = response.xpath('//*[@id="main-content"]/div/div/span[1]/text()').extract_first().split()[2]
        this_page = response.xpath('//*[@id="main-content"]/div/div/span[1]/text()').extract_first().split()[0]
        next_page = int(this_page) + 1

        if next_page <= int(total_page):
            next_page_url = 'http://www.allitebooks.org/page/{}'.format(next_page)
            yield scrapy.Request(url=next_page_url,callback=self.parse)

        # if next_page in range(1,3):
        #     next_page_url = 'http://www.allitebooks.org/page/{}'.format(next_page)
        #     yield scrapy.Request(url=next_page_url, callback=self.parse)


    def detail_parse(self,response):                # 解析每一本书的详细信息。
        item = ItebooksScrapyItem()

        tiltle = response.xpath('//*[@id="main-content"]/div/article/header/h1/text()').extract_first()

        book_detail = response.xpath('//*[@id="main-content"]/div/article//div[@class="book-detail"]')
        author = book_detail.xpath('.//dd[1]/a/text()').extract()
        author = ','.join(author)
        isbn = book_detail.xpath('.//dd[2]/text()').extract_first()
        year = book_detail.xpath('.//dd[3]/text()').extract_first()
        pages = book_detail.xpath('.//dd[4]/text()').extract_first()
        language = book_detail.xpath('.//dd[5]/text()').extract_first()
        file_size = book_detail.xpath('.//dd[6]/text()').extract_first()
        category = book_detail.xpath('.//dd[8]/a/text()').extract()
        category = re.sub('\s+\W\s+',' ',' '.join(category))                 # \s 不可见字符 \W 字母数字和下划线

        thumbnail = response.xpath('//*[@id="main-content"]/div/article/header/div/div[1]/a/img/@src').extract_first()
        pdf_download_url = response.xpath('//*[@id="main-content"]/div/article/footer/div/span[1]/a/@href').extract_first().replace(' ','%20')

        # book_description = response.xpath('//*[@id="main-content"]/div/article/div[1]/p[1]/text()').extract()

        item['title'] = tiltle
        item['author'] = author
        item['isbn'] = isbn
        item['year'] = year
        item['pages'] = pages
        item['language'] = language
        item['file_size'] = file_size
        item['category'] = category
        item['thumbnail'] = thumbnail
        item['pdf_download_url'] = pdf_download_url

        yield item



