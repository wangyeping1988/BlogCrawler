# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class BlogcrawlerSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class BlogcrawlerDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # request.cookies = {
        #     '.CNBlogsCookie': '6E0D581D816B40292F2CB163F9E2F6103933AE513E86496338B4D8098A447EF63939A0742F7BE1D09364AC1F46272E1B53175A0051B2F2E21476A6051F5FDD91E83A0AED5B2DA4AE02AD96225882AAA12602975F5AB90A169A851961F9B37D620F8C4D34',
        #     '.Cnblogs.AspNetCore.Cookies': 'CfDJ8BQYbW6Qx5RFuF4UTI7QvU118ut7nAbYfnRl0pAOtKCjq7-cwYn6CHWAbA4QwiOkwSvZ1jQu1PYse-z8i-D_Sl-rkl63Nvg_1w-vFssT77vMeEvCbSy2uwWYWHizRZbSazW4aoSLECfVWxioywacv3ZCzryhWkSfV2OKd-6EmsAnijvZ59eW1kYNH1keRodIMGM7k9Il2OvnOVOWSQysJbQPoYrR1uvHPY62avfQdQVhjHt7JhXhz5euovH6kVgZqFeIjUTCyqR6jc1LfS488Kr7-wVb-VMoLGYJFHKW_P2gEwzEImLJg3vYU-_Pp0NH333rhEiKaDnIHS3Y-WUpgaY9tAXSswLYTPFWCuBAe5SeY9nbRQqU9EJuix_fA0StJaNS1Nbc9MoW4LhRxctWJ_8HmnKhjuKW40d4bewALIJpJYot2X8FsS-NTr0LaPsJ4rAAS-zp4K9vlpKW_SsPe29STe_GJ0VKB0p2C18sX7WC',
        #     'SERVERID': '04ead23841720026ba009cb4f597ec8c|1566653061|1566652046',
        #     '__gads': 'ID=ae065093c3816478:T=1523979454:S=ALNI_MYA9AUiW8F72qKRLOTLGedFqt2nLw',
        #     '_ga': 'GA1.2.1968144735.1498924730',
        #     '_gid': 'GA1.2.466366568.1566609068'
        # }

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
