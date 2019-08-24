# -*- coding: utf-8 -*-
import scrapy

from BlogCrawler.items import CnblogsPostItem


class CnblogsSpider(scrapy.Spider):
    # spider name
    name = 'cnblogs'

    # allowed domains
    allowed_domains = ['i.cnblogs.com']

    # entry urls
    start_urls = [
        'https://i.cnblogs.com'
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
        yield scrapy.Request(
            self.start_urls[0],
            cookies={
                '.CNBlogsCookie': '6E0D581D816B40292F2CB163F9E2F6103933AE513E86496338B4D8098A447EF63939A0742F7BE1D09364AC1F46272E1B53175A0051B2F2E21476A6051F5FDD91E83A0AED5B2DA4AE02AD96225882AAA12602975F5AB90A169A851961F9B37D620F8C4D34',
                '.Cnblogs.AspNetCore.Cookies': 'CfDJ8BQYbW6Qx5RFuF4UTI7QvU118ut7nAbYfnRl0pAOtKCjq7-cwYn6CHWAbA4QwiOkwSvZ1jQu1PYse-z8i-D_Sl-rkl63Nvg_1w-vFssT77vMeEvCbSy2uwWYWHizRZbSazW4aoSLECfVWxioywacv3ZCzryhWkSfV2OKd-6EmsAnijvZ59eW1kYNH1keRodIMGM7k9Il2OvnOVOWSQysJbQPoYrR1uvHPY62avfQdQVhjHt7JhXhz5euovH6kVgZqFeIjUTCyqR6jc1LfS488Kr7-wVb-VMoLGYJFHKW_P2gEwzEImLJg3vYU-_Pp0NH333rhEiKaDnIHS3Y-WUpgaY9tAXSswLYTPFWCuBAe5SeY9nbRQqU9EJuix_fA0StJaNS1Nbc9MoW4LhRxctWJ_8HmnKhjuKW40d4bewALIJpJYot2X8FsS-NTr0LaPsJ4rAAS-zp4K9vlpKW_SsPe29STe_GJ0VKB0p2C18sX7WC',
                'SERVERID': '04ead23841720026ba009cb4f597ec8c|1566653061|1566652046',
                '__gads': 'ID=ae065093c3816478:T=1523979454:S=ALNI_MYA9AUiW8F72qKRLOTLGedFqt2nLw',
                '_ga': 'GA1.2.1968144735.1498924730',
                '_gid': 'GA1.2.466366568.1566609068'
            },
            callback=self.parse
        )

    def parse(self, response):
        """1. post list page"""
        post_list_items = response.xpath('//tr[contains(@id,"post-row-")]')
        for postListItem in post_list_items:
            try:
                tr_id = postListItem.xpath('@href').extract_first()
                if tr_id:
                    item = CnblogsPostItem()
                    item['id'] = tr_id[9:len(tr_id)]
                    yield item
            except(IndexError, TypeError):
                continue
