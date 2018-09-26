# coding:utf-8
from python.bdbk import html_outputer, html_parser, html_downloader, url_manager

# import url_manager, html_downloader, html_parser, html_outputer

print("爬虫百度百科调度入口")

# 创建爬虫类
class SpiderMain(object):

    # 初始化 url管理器 html下载器 解析器 输出器
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.output = html_outputer.HtmlOutput()


def craw(urls, downloader, parser, output, root_url):
    # 计数
    count = 1
    # 添加url到url管理器中
    urls.add_new_url(root_url)
    # 判断是否有新的URL
    while urls.has_new_url():
        try:

            # 获取新的URL
            new_url = urls.get_new_url()
            print('crawler %d : %s' % (count, new_url))
            # 下载html页面数据
            html_cont = downloader.download(new_url)
            # 解析页面得到新的url列表，新的数据
            new_urls, new_data = parser.parser(new_url, html_cont)
            # 把解析到的url数组批量添加到url管理器中
            urls.add_new_urls(new_urls)
            # 收集数据
            output.collect_data(new_data)
            # 爬虫1000页面
            if count == 50:
                break
            count = count + 1

        except Exception as e:
            print('Crawler Failed ', e)

    output.output_html()


if __name__ == '__main__':
    # 入口URL 百度百科地址
    root_url = "http://baike.baidu.com/item/Python"
    # 创建爬虫
    obj_spider = SpiderMain()
    # 启动爬虫
    craw(obj_spider.urls, obj_spider.downloader, obj_spider.parser, obj_spider.output, root_url)