from 模板.crawler_template import Runner

r = Runner(
    keywords=['望城县', '长沙市望城区', '望城区档案'],
    # url_template='http://so.voc.com.cn/cse/search?q={kw}&p={page}&s=7639422230623402302&sti=1440',
    url_template='http://so.voc.com.cn/cse/search?q={kw}&p={page}&s=7639422230623402302',
    links_xpath='//h3[@class="c-title"]/a/@href',
    paragraph_xpath_list=[
        '//div[@id="content"]//p/text()',
        '//div[@class="nei"]/ct/p//text()',
    ],
    debug=True,
    headless=True,
    raise_exception=False,
    title_xpath_list=[
        '//h1/text()',
    ],
    start_page=0
).run()
