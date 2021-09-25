from 模板.crawler_template import Runner

r = Runner(
    keywords=['望城县', '长沙市望城区', '望城区档案'],
    url_template='http://searching.hunan.gov.cn/hunan/971206000/news?q={kw}&searchfields=&sm=1&columnCN=&iszq=&aggr_iszq=&p={page}&timetype=timeqb',
    links_xpath='//div[@class="title "]/a/@href',
    paragraph_xpath_list=[
        '//div[@class="pages_content TRS_Editor"]/div//p//text()'
    ],
    debug=False,
    headless=True,
    raise_exception=False,
    title_xpath_list=[
        '//h1/text()',
    ]
).run()
