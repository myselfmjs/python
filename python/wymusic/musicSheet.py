from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from urllib import parse
import urllib
import random
import requests



def get_html(url):
    # 头问题参数
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent':user_agent}
    # 下载HTML
    req = urllib.request.Request(url,headers=headers)
    response = urlopen(req)
    html = response.read()
    return html


def html_cont(html):
    #歌单ID
    sheetId_List = []
    # 解析HTML页面
    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    links = soup.find_all(href = re.compile('playlist'))
    print(len(links))
    print(soup)
    for link in links:
        sheetId = re.findall(r'\d+$',link['href'])
        if sheetId !='':
            sheetId_List.append(sheetId)
    #去重
    #sheetId_List = list(set(sheetId_List))

    return sheetId_List

# 展示数据
def output_html(datas):

    fout = open('output.html', 'w',encoding="utf-8")

    fout.write('<html>')
    fout.write('<head>')
    fout.write('<meta http-equiv="Content-Type" content="text/html;charset=utf-8">')
    fout.write('</head>')
    fout.write('<body>')
    fout.write('<table border="1">')
    for data in datas:
        fout.write('<tr>')
        fout.write('<td>%s</td>' % data['title'])
        fout.write('<td>%s</td>' % data['strong'])
        fout.write('<td>%s</td>' % data['user'])
        fout.write('<td>%s</td>' % data['time'])
        fout.write('</tr>')
    fout.write('</table>')
    fout.write('</body>')
    fout.write('</html>')

    fout.close()

if __name__ == '__main__':
    # 歌单页数
    page_count = 2
    #网易地址
    BASE_URL = 'http://music.163.com/'
    # 歌单url
    page_url = 'http://music.163.com/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset='

    sheet_songList = []
    sheet_song = {}

    for i in  range(0,page_count):
        url = page_url + str(i * 35)
        html_cont = get_html(url)
        #soup = BeautifulSoup(requests.session().get(url).content)
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        linkList = soup.findAll('a', attrs={'class': 'tit f-thide s-fc0'})
        print(linkList)
        for link in linkList:
            sheetId = BASE_URL + link['href']
            sheet_Html = get_html(sheetId)
            sheet_cont = BeautifulSoup(sheet_Html, 'html.parser', from_encoding='utf-8')
            sheet_name = sheet_cont.find('h2', attrs={'class': 'f-ff2 f-brk'}).text
            sheet_time = sheet_cont.find('span', attrs={'class': 'time s-fc4'}).text
            strong = sheet_cont.find('strong', attrs={'class': 's-fc6'}).text
            user_name = sheet_cont.find('a',attrs={'class': 's-fc7'}).text
            comment_text = sheet_cont.find('div',attrs={'class': 'cnt f-brk'}).text
            sheet_song['title'] = sheet_name
            sheet_song['strong'] = strong
            sheet_song['user'] = user_name
            sheet_song['time'] = sheet_time
            sheet_songList.append(sheet_song)
            print('歌单：'+ sheet_name + '   播放量：' + strong +
                  '   创建人：' + user_name + '   创建时间：' + sheet_time)

    output_html(sheet_songList)
