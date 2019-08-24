# -*- coding: utf-8 -*-
import scrapy

from BlogCrawler.items import CnblogsPostItem


class CnblogsSpider(scrapy.Spider):
    # spider name
    name = 'cnblogs'

    # allowed domains
    allowed_domains = ['cnblogs.com']

    # entry urls
    start_urls = [
        'https://www.cnblogs.com/wyp1988/'
    ]

    def parse(self, response):
        """1. post list page"""
        # post_list_items = response.xpath('//tr[contains(@id,"post-row-")]')
        post_list_items = response.xpath('//a[@class="c_b_p_desc_readmore"]')
        for postListItem in post_list_items:
            try:
                tr_id = postListItem.xpath('@href').extract_first()
                if tr_id:
                    item = CnblogsPostItem()
                    item['id'] = tr_id[9:len(tr_id)]
                    yield item
            except(IndexError, TypeError):
                continue
