# coding:utf-8
from python.wymusic import html_outputer, html_parser, html_downloader
from datetime import datetime
import time



# 创建爬虫类
class SpiderMain(object):

    # 初始化 url管理器 html下载器 解析器 输出器
    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.output = html_outputer.HtmlOutput()

# def get_time_now():
#     now = int(time.time())
#     #转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
#     timeStruct = time.localtime(now)
#     strTime = time.strftime("%Y-%m-%d %H:%M:%S", timeStruct)

def cal_difftime(time1, time2):
    sec = (time2-time1).seconds
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    difftime = "%02d时%02d分%02d秒" % (h, m, s)
    return difftime

def craw(downloader, parser, output, root_url):


    print("爬取网易云歌单开始：" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    start_time = datetime.now()

    # 歌单页数(单页有35个歌单，现在共有41页歌单)
    page_count = 42
    # 歌单所在页面初始url
    page_url = 'http://music.163.com/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset='

    for i in  range(0,page_count):
        # 获取歌单所在页的 url
        new_url = page_url + str(i * 35)
        # 下载html页面数据
        html_cont = downloader.download(new_url)
        # 解析页面得到新的url列表，新的数据
        linkList = parser.parser_url(html_cont)
        for link in linkList:
            # 拼接歌单url
            sheet_url = root_url + link['href']
            # 下载歌单页
            sheet_cont = downloader.download(sheet_url)
            # 获取数据
            data = parser.parser_sheet(sheet_url,sheet_cont)
            # 保存数据
            output.collect_data(data)

    # 保存为HTML
    output.output_html()
    # 保存为 xls
    output.out_excel()

    end_time = datetime.now()
    use_time = cal_difftime(start_time,end_time)
    print("爬取网易云歌单结束 用时：" + use_time)


if __name__ == '__main__':
    # 入口URL 网易地址
    root_url = 'http://music.163.com/'
    # 创建爬虫
    obj_spider = SpiderMain()
    # 启动爬虫
    craw(obj_spider.downloader, obj_spider.parser, obj_spider.output, root_url)