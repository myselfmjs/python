# coding:utf-8

from bs4 import BeautifulSoup
import re
from urllib import parse


class HtmlParser(object):


    def _get_new_data(self, page_url, soup):
        # 定义一个dict 集合
        res_data = {}
        # 正则规则-取得创建日期字符串
        rule = r'\d*-\d*-\d*'
        compiled_rule=re.compile(rule)

        # 歌单URL
        res_data['url'] = page_url
        # 歌单名称
        sheet_name = soup.find('h2', attrs={'class': 'f-ff2 f-brk'}).text
        res_data['title'] = sheet_name
        # 播放量
        strong = soup.find('strong', attrs={'class': 's-fc6'}).text
        res_data['strong'] = strong
        #创建者
        user_name = soup.find('a',attrs={'class': 's-fc7'}).text
        res_data['user'] = user_name
        # 创建时间
        sheet_time = soup.find('span', attrs={'class': 'time s-fc4'}).text
        sheet_time = ''.join(compiled_rule.findall(sheet_time))
        res_data['time'] = sheet_time

        print('歌单：'+ sheet_name + '   播放量：' + strong +
              '   创建人：' + user_name + '   创建时间：' + sheet_time)

        return res_data


    # 解析 当前页的所有歌单URL
    def parser_url(self,html_content):
        if  html_content is None:
            return
        # 使用BeautifulSoup 解析html页面
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        sheet_a = soup.findAll('a', attrs={'class': 'tit f-thide s-fc0'})

        return  sheet_a


    # 解析歌单页面
    def parser_sheet(self, sheet_url, sheet_content):

        if sheet_url is None or sheet_content is None:
            return

        # 使用BeautifulSoup 解析html页面
        soup = BeautifulSoup(sheet_content, 'html.parser', from_encoding='utf-8')

        new_data = self._get_new_data(sheet_url, soup)
        return new_data