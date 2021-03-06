# -*- coding: utf-8 -*-
import scrapy

from BlogCrawler.items import CnblogsPostItem
from scrapy.http import Request


class CnblogsSpider(scrapy.Spider):
    # spider name
    name = 'cnblogs'

    # allowed domains
    allowed_domains = ['i1.cnblogs.com']

    # entry urls
    start_urls = [
        'https://i1.cnblogs.com/posts',
        'https://i1.cnblogs.com/posts?page=2',
        'https://i1.cnblogs.com/posts?page=3',
        'https://i1.cnblogs.com/posts?page=4',
        'https://i1.cnblogs.com/posts?page=5',
        'https://i1.cnblogs.com/posts?page=6',
        'https://i1.cnblogs.com/posts?page=7',
        'https://i1.cnblogs.com/posts?page=8',
        'https://i1.cnblogs.com/posts?page=9',
        'https://i1.cnblogs.com/posts?page=10',
        'https://i1.cnblogs.com/posts?page=11',
        'https://i1.cnblogs.com/posts?page=12',
        'https://i1.cnblogs.com/posts?page=13',
        'https://i1.cnblogs.com/posts?page=14',
        'https://i1.cnblogs.com/posts?page=15',
        'https://i1.cnblogs.com/posts?page=16',
        'https://i1.cnblogs.com/posts?page=17',
        'https://i1.cnblogs.com/posts?page=18',
        'https://i1.cnblogs.com/posts?page=19',
        'https://i1.cnblogs.com/posts?page=20',
        'https://i1.cnblogs.com/posts?page=21',
        'https://i1.cnblogs.com/posts?page=22',
        'https://i1.cnblogs.com/posts?page=23',
        'https://i1.cnblogs.com/posts?page=24',
        'https://i1.cnblogs.com/posts?page=25',
        'https://i1.cnblogs.com/posts?page=26',
        'https://i1.cnblogs.com/posts?page=27',
        'https://i1.cnblogs.com/posts?page=28',
        'https://i1.cnblogs.com/posts?page=29',
        'https://i1.cnblogs.com/posts?page=30',
        'https://i1.cnblogs.com/posts?page=31',
        'https://i1.cnblogs.com/posts?page=32',
        'https://i1.cnblogs.com/posts?page=33',
        'https://i1.cnblogs.com/posts?page=34',
        'https://i1.cnblogs.com/posts?page=35',
        'https://i1.cnblogs.com/posts?page=36',
        'https://i1.cnblogs.com/posts?page=37',
        'https://i1.cnblogs.com/posts?page=38',
        'https://i1.cnblogs.com/posts?page=39',
        'https://i1.cnblogs.com/posts?page=40'
    ]

    # def start_requests(self):
    #     url = 'https://account.cnblogs.com/signin'
    #     data = {
    #         'email': 'wangyeping1988',
    #         'password': 'bk1517P@ssword',
    #     }
    #     request = scrapy.FormRequest(url, formdata=data, callback=self.parse_page)
    #     yield request
    #
    # def parse_page(self, response):
    #     url2 = 'http://www.renren.com/880792860/profile'
    #     request = scrapy.Request(url2 ,callback=self.parse_profile)
    #     yield request

    # def start_requests(self):
    #     headers = {
    #         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"}
    #
    #     cookies = {
    #         '.CNBlogsCookie': '6E0D581D816B40292F2CB163F9E2F6103933AE513E86496338B4D8098A447EF63939A0742F7BE1D09364AC1F46272E1B53175A0051B2F2E21476A6051F5FDD91E83A0AED5B2DA4AE02AD96225882AAA12602975F5AB90A169A851961F9B37D620F8C4D34',
    #         '.Cnblogs.AspNetCore.Cookies': 'CfDJ8BQYbW6Qx5RFuF4UTI7QvU118ut7nAbYfnRl0pAOtKCjq7-cwYn6CHWAbA4QwiOkwSvZ1jQu1PYse-z8i-D_Sl-rkl63Nvg_1w-vFssT77vMeEvCbSy2uwWYWHizRZbSazW4aoSLECfVWxioywacv3ZCzryhWkSfV2OKd-6EmsAnijvZ59eW1kYNH1keRodIMGM7k9Il2OvnOVOWSQysJbQPoYrR1uvHPY62avfQdQVhjHt7JhXhz5euovH6kVgZqFeIjUTCyqR6jc1LfS488Kr7-wVb-VMoLGYJFHKW_P2gEwzEImLJg3vYU-_Pp0NH333rhEiKaDnIHS3Y-WUpgaY9tAXSswLYTPFWCuBAe5SeY9nbRQqU9EJuix_fA0StJaNS1Nbc9MoW4LhRxctWJ_8HmnKhjuKW40d4bewALIJpJYot2X8FsS-NTr0LaPsJ4rAAS-zp4K9vlpKW_SsPe29STe_GJ0VKB0p2C18sX7WC',
    #         'SERVERID': '04ead23841720026ba009cb4f597ec8c|1566653061|1566652046',
    #         '__gads': 'ID=ae065093c3816478:T=1523979454:S=ALNI_MYA9AUiW8F72qKRLOTLGedFqt2nLw',
    #         '_ga': 'GA1.2.1968144735.1498924730',
    #         '_gid': 'GA1.2.466366568.1566609068'
    #     }
    #
    #     yield Request(detailUrl, headers=headers, cookies=cookies, callback=self.detail_parse, meta={'myItem': item},
    #                   dont_filter=True)

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                cookies={
                    '.CNBlogsCookie': 'AAA49C92BF3B1871B6ACCB924D521C61DA4F061BFA9A8365048BFE1F4FACB19DCF8C739C9AEAADD2B6E9873BD9E2FB6B8C574CF69670BB100967F0D677F55B116C3C588B1D7E4EDF379BB8CCA61D45DF30F67D15E86C3CEB03051F59D7AD47B6E07C33A5'
                },
                callback=self.parse
            )

    def parse(self, response):
        """1. post list page"""
        edit_page_url = 'https://i1.cnblogs.com/EditPosts.aspx?postid={0}&update=1'
        post_list_items = response.xpath('//tr[contains(@id,"post-row-")]')
        for postListItem in post_list_items:
            try:
                tr_id = postListItem.xpath('@id').extract_first()
                if tr_id:
                    yield Request(edit_page_url.format(tr_id[9:len(tr_id)]), callback=self.parse_edit_page)
            except(IndexError, TypeError):
                continue


    def parse_edit_page(self, response):
        """2. post edit page"""
        post_title = response.xpath('//input[@id="Editor_Edit_txbTitle"]/@value').extract_first()
        post_content = response.xpath('//textarea[@id="Editor_Edit_EditorBody"]').xpath('text()').extract_first()
        if post_content[0:2] == '\r\n':
            post_content = post_content[2:len(post_content)]
        item = CnblogsPostItem()
        item['title'] = post_title
        item['content'] = post_content
        yield item