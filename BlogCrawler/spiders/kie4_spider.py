# -*- coding: utf-8 -*-
import scrapy

from BlogCrawler.items import Kie4Item
from scrapy.http import Request


class Kie4Spider(scrapy.Spider):
    # spider name
    name = 'kie4'

    # allowed domains
    allowed_domains = ['www.kie4.com', 'www.jai3.com']

    # entry urls
    start_urls = [
        'https://www.jai3.com/tupian/list-亚洲图片-1.html'
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

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield scrapy.Request(
    #             url,
    #             cookies={
    #                 '.CNBlogsCookie': '514266FBFC64C1F802AD4C83B4A675EC58909E5B8B5FBFCF81DAD7D4A9F8545EE30C7C2C5B39E2FBDCE608E957D3E75998D0B092B743ED7C2263C896E5E5C49FB0F500C6B10626C939AE8891D6B1C32A6864F2366FED6ED33541A67679DA24726676FD04 '
    #             },
    #             callback=self.parse
    #         )

    def parse(self, response):
        """1. post list page"""
        detail_page_url = 'https://www.jai3.com{0}'
        post_list_items = response.xpath('//div[@class="text-list-html"]//li/a[contains(@href, "/tupian/")]')
        for postListItem in post_list_items:
            try:
                href = postListItem.xpath('@href').extract_first()
                if href:
                    yield Request(detail_page_url.format(href), callback=self.parse_detail_page)
            except(IndexError, TypeError):
                continue

    def parse_detail_page(self, response):
        """2. post edit page"""
        # < img class ="videopic lazy" src="https://img.i1m2g3e.com/passimg/tx/72811/01.jpg" data-original="https://img.i1m2g3e.com/passimg/tx/72811/01.jpg" title="笛木優子靓丽写真(2)1" style="" >
        # < img class ="videopic lazy" src="/assets/images/default/loading/248x355.jpg" data-original="https://img.i1m2g3e.com/passimg/tx/72811/01.jpg" title="笛木優子靓丽写真(2)1" >
        title = response.xpath('//div[@class="content"]//img/@title').extract_first()
        links = response.xpath('//div[@class="content"]//img/@data-original').extract()
        item = Kie4Item()
        item['title'] = title
        item['links'] = links
        yield item