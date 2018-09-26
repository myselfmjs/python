# coding:utf-8

from urllib.request import urlopen
print ("下载HTML")


class HtmlDownloader(object):

    def download(self, url):
        # 判断是否为空
        if url is None:
            return None
        # 下载url
        response = urlopen(url)
        # 判断返回结果是否为200
        if response.getcode() != 200:
            return None
        # 成功 返回页面内容
        return response.read()