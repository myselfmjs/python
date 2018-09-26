# coding:utf-8

from bs4 import BeautifulSoup
import re
from urllib import parse

print("HTML 解析器")


class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):

        # 创建一个集合保存页面解析出来的所有url
        new_urls = set()
        # /item/  词条url
        links = soup.find_all('a', href=re.compile(r'/item/'))
        for link in links:
            # 获取连接
            new_url = link['href']
            # url拼接
            new_full_url = parse.urljoin(page_url, new_url)
            # print 'new_full_url', new_full_url
            # 添加到集合中url
            new_urls.add(new_full_url)
        return new_urls


    def _get_new_data(self, page_url, soup):
        # 定义一个dict 集合
        res_data = {}

        res_data['url'] = page_url
        # < dd class ="lemmaWgt-lemmaTitle-title" >< h1 > 自由软件 < / h1 >
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()
        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()

        return res_data


    # 解析器
    def parser(self, page_url, html_content):

        if page_url is None or html_content is None:
            return

        # 使用BeautifulSoup 解析html页面
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data