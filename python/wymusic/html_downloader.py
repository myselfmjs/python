# coding:utf-8
import urllib

from urllib.request import urlopen

class HtmlDownloader(object):

    def download(self, url):
        # 判断是否为空
        if url is None:
            return None
        # 头问题参数
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent':user_agent}
        # 下载url
        req = urllib.request.Request(url,headers=headers)
        response = urlopen(req)
        # 判断返回结果是否为200
        if response.getcode() != 200:
            return None
        # 成功 返回页面内容
        return response.read()