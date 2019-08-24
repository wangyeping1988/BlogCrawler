# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import os


class BlogcrawlerPipeline(object):
    def process_item(self, item, spider):
        try:
            post_file = codecs.open('posts' + os.path.sep + item['title'] + '.md', 'wb', encoding='utf-8')
            post_file.write(item['content'])
            post_file.close()
        except(IndexError, TypeError):
            pass

        return item
