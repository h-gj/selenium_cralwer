from 模板.crawler_template import Runner

r = Runner(
    keywords=['望城县', '长沙市望城区', '望城区档案'],
    url_template='https://news-search.rednet.cn/Search?q={kw}&p={page}',
    links_xpath='//div[@class="result-footer"]/a/@href',
    paragraph_xpath_list=[
        '//article//p/text()',
        '//div[@class="nei"]/ct/p//text()',
    ],
    debug=True,
    headless=False,
    raise_exception=False,
    title_xpath_list=[
        '//h1/text()',
    ]
).run()
