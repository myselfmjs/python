# coding:utf-8

print ("URL管理器")


class UrlManager(object):

    # 初始化url容器（set集合）
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    # 添加一个新的待爬取url
    def add_new_url(self, url):

        if url is None:
            return

        # 判断url不在新的url集合中也不再旧的url集合中 说明是一个全新的url
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 批量添加解析页面的URL
    def add_new_urls(self, urls):

        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    # 判断是否有新的待爬取的url
    def has_new_url(self):
        # 如果新的url集合里面len不等于0 说明有待爬取的url
        return len(self.new_urls) != 0

    # 获得url地址
    def get_new_url(self):
        # 获取url并移除当前url
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url