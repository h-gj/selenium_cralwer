from threading import Thread

import requests

from 模板.crawler_template import Runner


class RenMinRiBaoRunner(Runner):
    def get_page_item_links(self, kw, page=1, previous_links=None, total_links=None):
        if not total_links:
            total_links = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
        }
        self.url_template = 'http://search.people.cn/api-search/front/search'
        json = {"key": kw, "page": page, "limit": 10, "hasTitle": True, "hasContent": True, "isFuzzy": True, "type": 0,
                "sortType": 2, "startTime": 0, "endTime": 0}
        content = requests.post(self.url_template, headers=headers, json=json).json()
        records = content.get('data').get('records')
        links = [record.get('url') for record in records]
        # print('links', links)
        # links = html.xpath(self.links_xpath)
        if not links:
            return total_links

        for link in links:
            # print('put %s into queue' % link)
            self.queue.put(link)

        # print('links', links)
        total_links += links
        return self.get_page_item_links(kw, page=page + 1, previous_links=links[:], total_links=total_links[:])


r = RenMinRiBaoRunner(
    keywords=['望城县', '长沙市望城区', '望城区档案'],
    url_template='',
    paragraph_xpath_list=[
        '//div[@class="rm_txt_con cf"]/p//text()',
        '//div[@class="clearfix w1000_320 text_con"]//p/text()',
        '//div[contains(@class, "clearfix")]//p/text()',
    ],
    debug=True,
    raise_exception=True,
    title_xpath_list=[
        '//h1/text()',
        '//h2/text()',
    ]
    # test_links=['http://society.people.com.cn/n1/2020/1219/c1008-31972132.html', 'http://hb.people.com.cn/n2/2020/1219/c194063-34483122.html', 'http://hn.people.com.cn/n2/2021/0506/c356887-34711408.html', 'http://hn.people.com.cn/n2/2021/0722/c356886-34832796.html', 'http://hn.people.com.cn/n2/2020/1229/c356887-34500737.html', 'http://gz.people.com.cn/n2/2021/0423/c361324-34691384.html', 'http://finance.people.com.cn/n1/2021/0619/c1004-32134821.html', 'http://hn.people.com.cn/n2/2021/0218/c356886-34581110.html', 'http://hn.people.com.cn/n2/2021/0727/c336521-34840279.html', 'http://hn.people.com.cn/n2/2021/0714/c356886-34819827.html']
).run()
