import scrapy
import logging
from meteor.items import MeteorItem
from scrapy_splash import SplashRequest

def script(year, month):
    _script = """
    function main(splash, args)
        splash.images_enabled=false
        assert(splash:go(args.url))
        assert(splash:wait(args.wait))
        js = string.format("document.querySelector('a[dataval=\\"{}\\"]').click();", args.page)
        splash:runjs(js)
        assert(splash:wait(args.wait+1))
        js = string.format("document.querySelector('ul.select-down-list > li > a[dataval=\\"{}\\"]').click();", args.page)
        splash:runjs(js)
        assert(splash:wait(args.wait+1))
        return splash:html()
    end
    """.format(year, month)
    return _script

class TianqiSpider(scrapy.Spider):
    count = 0
    name = 'tianqi'
    allowed_domains = ['tianqi.2345.com']
    start_urls = ['https://tianqi.2345.com/wea_history/71257.htm']
    year = 2022
    month = 8
    MINYEAR = 2012
    MINMONTH = 1

    STOP_MONTH = 4
    STOP_YEAR = 2012

    def start_requests(self):
        for url in self.start_urls:
            print(script(2021,12))
            yield SplashRequest(url, self.parse, endpoint='execute',
                                    args={ 'wait': 1, 'lua_source': script(self.year,self.month)} )

    def parse(self, response):
        self.count += 1
        logging.info(u'----------使用splash爬取tianqi网异步加载内容-----------')
        # print("url = ", response.url)
        # a = response.xpath("//a[@id='js_prevMonth' and @class='no-data-btn']").extract()
        # # a = response.xpath("//a[@id='js_nextMonth' and @class='no-data-btn']").extract()
        # if len(a) != 0:
        #     print("next/prev is no-data-btn")
        #     return
        for workList in response.xpath("//table[contains(@class, 'history-table')]"):
            # print(workList)
            topFive = workList.xpath("//tr/td/text()").extract()
            sixth = workList.xpath("//tr/td/span/text()").extract()
            for i in range(len(sixth)):
                item = MeteorItem()
                item["Date"] = topFive[i*5+0]
                item["HighestTemp"] = topFive[i*5+1]
                item["LowestTemp"] = topFive[i*5+2]
                item["WindDest"] = topFive[i*5+3]
                item["Weather"] = topFive[i*5+4]
                item["AirQual"] = sixth[i]
                yield item
            break
        # print("extracted: ", topFive[0])

        # for url in self.start_urls:
        print("Next paging..", self.count)
        self.month -= 1
        if self.month == self.STOP_MONTH and self.year == self.STOP_YEAR:
            return

        if self.month < self.MINMONTH:
            self.month = 12
            self.year -= 1
            if self.year < self.MINYEAR:
                return 
                
        yield SplashRequest(self.start_urls[0], self.parse, endpoint='execute',
                    args={ 'wait': 1, 'lua_source': script(self.year, self.month)} ,dont_filter=True)
