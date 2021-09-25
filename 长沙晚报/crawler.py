from 模板.crawler_template import Runner

r = Runner(
    keywords=['望城县', '长沙市望城区', '望城区档案'],
    url_template='https://so.icswb.com/default.php?mod=search&m=no&syn=no&f=_all&s=s_show_date_DESC&temp=&p={page}&ps=20&site_id=2&range=&search_target=1&search_key={kw}&search_column=&search_channel_id=0',
    links_xpath='//h3/a/@href',
    paragraph_xpath_list=[
        '//article[@class="am-article"]//p/text()',
        '//div[@class="nei"]/ct/p//text()',
    ],
    debug=True,
    headless=True,
    raise_exception=False,
    title_xpath_list=[
        '//h1/text()',
    ]
).run()
