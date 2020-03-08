# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json,os
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class MyImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):

        yield Request(item['thumbnail'])

    def file_path(self, request, response=None, info=None):
        image_name = request.url.split('/')[-1]

        return image_name


class JsonSavedPipeline(object):
    def __init__(self):
        path = os.getcwd() + '/itEbooks_Scrapy/output/'
        self.file = codecs.open(path + 'books_info.json','w',encoding="utf-8")

    def process_item(self,item,spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(lines)
        return item
    def spider_closed(self,spider):
        self.file.close()

class ItebooksScrapyPipeline(object):
    def process_item(self, item, spider):
        return item
