from login.items import LoginItem
import scrapy
from scrapy_splash import SplashRequest
import logging

script = """
function main(splash, args)
    splash.images_enabled=false
    splash:set_custom_headers({
        ["Cookie"] = 'mtuid-wk=7b3e81153845560ea94037ebd642d4; ubid-acbus-mtw=135-9770390-9556868; session-id-mtw=135-1422462-4790701; ws=f; s_cc=true; s_fid=57474DE6C7614E62-3AC01B875545F63A; search_page_size=ZFhKLyt0Z3NYdWNCNUY2b1FMbjhDQT09LS05eHdnSWNRcnNjTElnL1dVTGRnUkJRPT0=--8f22bd9b401b902767131999ad042dabc3237bab; qualified_filter=QVBEWjJnSGdsMTZPRHdHa0cwanlhUT09LS1oMzRhcVRiVGQ1ZjlsRXVJelM5WGVnPT0=--9d6e7ca08f0c0978fc74c6f4c07ee8c7e00925c6; masters_filter=SHVSdENVNEFMcmxnUVkyL2xJdEdPZz09LS0wTVY3UHZBY0FLd0VuOEV1a1JCZGpBPT0=--65757bca33effc9aaed25cc01ff964f2e52555d9; min_reward_filter=aWY2NkdLamwrOGpmdnhKRDkzMHBhQT09LS1XOVBwWS91TzdYMHBxblovbzdCQUd3PT0=--16c3d86983334f987b5b2c3e42c60d4bd291bff7; search_sort_key=ZEY0RjJWZ1U5NnVqUXh3ZlRsbC9OUFU0cWF2RlVoN2JQcm9ZVFhVa0lvND0tLVZ3SnJBTDJjc2tZK2t6elpBRFZIWWc9PQ==--e12c0e1f6c90453d4f685fb7c555fa9a7932c043; s_vnum=1637569030081&vn=3; s_invisit=true; session-id-time-mtw=2265866253l; session-token-mtw="qpetWRERnDnAJA6i5SqCHDJ5QL0zvbhfYvQVhBdQFrRYqpBUWqi6KjSSHCkd6FCZU2nA0ULvBQ8jW4r0RbiUEVnsq4nnUaP7CutZSIdxEBWiMB/lhHm5qyQGqVuK4MxvP4fKQeeIX3KcHuTaPybkvMPe4B5Tif0cKyGCA4YV+9BdA/DaRqsLsxq3P447fTmW9FM8DODB1A9YDAEygeAVvrXwgCX2Bkb87lJ6ve9LzZU="; x-acbus-mtw=rrW2ai8av07iuwV6A3vQshdcvc7XIQYwiFzPZnRBK0Plfd5guhC2O0dCM7ji6idn; at-acbus-mtw=Atza|IwEBIM8Lxlt64LTf-A2AepWlHTa6Xjl4R4mc-ypmVuYQPZXUETwJV5e-J9RKiH_LeI9H_q8noUoyL-fuYRQS4jPdIVNZz73-Gio8XN5q0KmWywkPgJGNTeG2TamwRjAOcnoZtIOjVXKPMj1wdfZ9c1LCH3VXkx-A3CbqDiCBNxqqMNDFCNqKoMA0h7JiMGyjN--s2wJEezBV3DWeNSpjGmkZ1OXygKpzhCwNrXyh9oHDjiCV4A; sess-at-acbus-mtw="/XjptSczT7Rz57479RXzt8p8CFaHeaSmWz6hoH5JG74="; s_nr=1635147506892-Repeat; _mechturk_session=Z0czNVlxS0xVVmpyQ3NTaTdIMUZYUmRLQWxVOXdtNHNBbUhxOUd3VVJGUFE3ajVpN0dFbEFGZE8vS2JJbGRPYWF3YVUxS0NYWjlmaHFLRzdJT1FueGFTa1BxeHgxM2E5RDdFa2lyUFVFUWNqSldVeWs3UU9BdU45TjBIV3dlVHBDMjExQTl6b2Q0T3BhL2lkTVBCUGFCYVQzNC94QytHaTJsalA2WFJXVkRDOVVEeXR4d2VRN2dTZ0Y0MUljMWlzMEFnMEtBZWpaL2kwbUE1Si80djVuOXJvVkFPR1AyeSszV3NGUDNoV1d4bTV4Z21XdDZpWVNhOGRPYXEyWFZFVkR6cHRXSFdRb1dJNld6OEFydnhRUlBmdndidVdNdkhRcjNIdWJQNlp6UlplSXUxYUFuVCtkTjB6YlFXSjRXUnJybk83Z2ZrVUZaRFlQWFV2SHZGZGVkZzVZQmFoWGwwOTU1VnhvcXdUSS9rPS0tTlNMeWhreHNNRlowQXROZTh6bDFoQT09--3d976828014e15e36202cea0c4bd1060865b6fc6; worker_goal=hits_submitted:0|hits_reward:0.0|submit_goal:0|reward_goal:0.0|is_submit_goal_updated:false|is_reward_goal_updated:false|goal_date:10/25/2021'
    })
    assert(splash:go(args.url))
    assert(splash:wait(args.wait))
    js = string.format("document.querySelector('span.expand-projects-button > a > i').click();", args.page)
    splash:runjs(js)
    assert(splash:wait(args.wait))
    return splash:html()
end
"""
splash_args = {
    'wait': 1,
    'lua_source': script
}

class WorkerSpider(scrapy.Spider):
    name = 'worker'
    allowed_domains = ['worker.mturk.com']
    start_urls = ['https://worker.mturk.com/?page_size=20&filters%5Bqualified%5D=false&filters%5Bmasters%5D=false&sort=num_hits_desc&filters%5Bmin_reward%5D=&page_number=1']
    visited_urls = []

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, endpoint='execute',
                                args=splash_args)

    def parse(self, response):
        logging.info(u'----------使用splash爬取worker网异步加载内容-----------')
        size = 0
        for workList in response.xpath("//li[contains(@class, 'hit-set-table-row')]"):
            item = LoginItem()
            Requester = workList.xpath(".//span[contains(@class,'requester-column')]/span/a/text()").get()
            item['Requester'] = Requester
            Title = workList.xpath(".//div/span[contains(@class,'project-name-column')]/text()").get()
            item['Title'] = Title 
            HITs = workList.xpath(".//div/span[contains(@class,'task-column')]/text()").get()
            item['HITs'] = HITs 
            Reward = workList.xpath(".//div/span[contains(@class, 'reward-column')]/text()").get()
            item['Reward'] = Reward 
            Created = workList.xpath(".//div/span[contains(@class, 'created-column')]/span/@title").get()
            item['Created'] = Created 
            Actions = workList.xpath(".//div/span[contains(@class, 'actions-column')]/span/span/a/text()").get()
            item['Actions'] = Actions
            Description = workList.xpath(".//div[contains(@class, 'expanded-row')]/div/div/div/div/p/text()").get()
            item['Description'] = Description
            TimeAllotted = workList.xpath(".//h6[text()='Time Allotted']/../text()").get()
            item['TimeAllotted'] = TimeAllotted
            Expires = workList.xpath(".//h6[text()='Expires']/../span/@title").get()
            item['Expires'] = Expires
            logging.info(Requester)
            logging.info(TimeAllotted)
            logging.info(Expires)
            size += 1
            yield item
            # break
        logging.info("There are " + str(size) + " selectors")
        # logging.info(response.body.decode())
        fh = open("write_data2.html", "w")
        fh.write(str(response.body.decode()))
        self.visited_urls.append(response.url)
        nextURL = response.xpath("//li[@class='page-item']/a/@href").extract()
        logging.info("Next, we can go " + str(nextURL))

        for url in nextURL:
            if url not in self.visited_urls:    
                yield SplashRequest(url, self.parse, endpoint='execute',
                                    args=splash_args)