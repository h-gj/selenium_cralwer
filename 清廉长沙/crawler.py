import requests
from 模板.crawler_template import Runner


class SelfRunner(Runner):
    def get_page_item_links(self, kw, page=0, total_links=None):
        if not total_links:
            total_links = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
            'Cookie': '_gscu_2138955816=32544007ji8gtf25; _gscbrs_2138955816=1; ICMS_VISIT_FLAG_COOKIE=2021-9-25_39009615; Hm_lvt_1addf79e03854c60736c4faedb476b73=1632544007; Hm_lpvt_1addf79e03854c60736c4faedb476b73=1632544007; _gscs_2138955816=32544007dgkyxx25|pv:4',
            'Referer': 'http://www.ljcs.gov.cn/search.html?searchkey=%E6%9C%9B%E5%9F%8E%E5%8E%BF',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Origin': 'http://www.ljcs.gov.cn'
        }
        self.url_template = 'http://www.ljcs.gov.cn/default.php?client=client&mod=document_news&f=interface&a=news_list'
        data = {
            'search_key': kw,
            'siteid': '1',
            'channel_id': '',
            'state': '30',
            'p': '%s' % page,
            'ps': '20',
            'is_encrypt': '0',
            'only_client': '0',
            'haschild': '0',
            'skip_index': '0'
        }
        res = requests.post(self.url_template, headers=headers, data=data).json()
        result = res.get('result')
        links = ['http://www.ljcs.gov.cn/' + item.get('DocumentNewsUrl') for item in result or []]
        print('links', links)
        # links = html.xpath(self.links_xpath)
        if not links:
            return total_links

        for link in links:
            # print('put %s into queue' % link)
            self.queue.put(link)

        # print('links', links)
        total_links += links
        return self.get_page_item_links(kw, page=page + 1, total_links=total_links[:])


r = SelfRunner(
    keywords=['望城区', '长沙市望城区', '望城区档案'],
    url_template='',
    paragraph_xpath_list=['//div[@class="rm_txt_con cf"]/p//text()',
                          '//div[@class="am-article-bd"]/div[contains(@style, "align") or @align!=""]',
                          '//div[@class="article"]//p//text()'
                          ],
    debug=False,
    headless=True,
    raise_exception=False,
    title_xpath_list=[
        '//h1/text()',
        '//div[@class="maintitle"]/text()'
    ]
    # test_links=['']
).run()
