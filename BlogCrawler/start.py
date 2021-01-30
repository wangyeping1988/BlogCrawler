import scrapy
from scrapy.crawler import CrawlerProcess

from BlogCrawler.spiders.kie4_spider import Kie4Spider
from spiders.cnblogs_spider import CnblogsSpider

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

# process.crawl(CnblogsSpider)
process.crawl(Kie4Spider)
process.start() # the script will block here until the crawling is finished