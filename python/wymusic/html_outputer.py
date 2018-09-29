# coding:utf-8

from xlwt import Workbook,Style

class HtmlOutput(object):

    def __init__(self):
        self.datas = []

    # 收集数据
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    # 展示数据
    def output_html(self):
        fout = open('output.html', 'w',encoding="utf-8")
        fout.write('<html>')
        fout.write('<head>')
        fout.write('<meta http-equiv="Content-Type" content="text/html;charset=utf-8">')
        fout.write('</head>')
        fout.write('<body>')
        fout.write('<table border="1">')
        fout.write('<tr>')
        fout.write('<td style="text-align:center">歌单名称</td>')
        fout.write('<td style="text-align:center">播放量</td>')
        fout.write('<td style="text-align:center">创建者</td>')
        fout.write('<td style="text-align:center">创建时间</td>')
        fout.write('</tr>')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td><a href = "%s">%s</a></td>' % (data['url'], data['title']))
            fout.write('<td>%s</td>' % data['strong'])
            fout.write('<td>%s</td>' % data['user'])
            fout.write('<td>%s</td>' % data['time'])
            fout.write('</tr>')
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        fout.close()


    # 展示数据 Excel
    def out_excel(self):
        # 创建 workbook 和 sheet
        workbook = Workbook(encoding='utf-8')
        sheet = workbook.add_sheet('music')
        # 标题名称
        row_name = ['歌单链接','歌单名称','播放量','创建者','创建时间']
        # 获取第一行 写入标题
        row = sheet.row(0)
        for num in range(len(row_name)):
            row.write(num,row_name[num])

        i_row = 1
        rows = self.datas
        for i in range(i_row,len(rows)+i_row):
            # 获得sheet 的第 i 行
            row_i = sheet.row(i)
            # Dict 转为 list
            values = list(rows[i-1].values())
            for j in range(len(values)):
                # 写入数据
                row_i.write(j,values[j])

        workbook.save('D:\\project\\python\\music.xls')






